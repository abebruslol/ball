from tkinter import*
import random
import time

screen = Tk()
screen.title("Name")
screen.resizable(False,False)
screen.wm_attributes('-topmost',1)
canvas = Canvas(screen ,width=500 ,height=500)

canvas.pack()
screen.update()

class Ball:
    def __init__(self,canvas,color,plate,score):
        self.hit_bottom = False
        self.plate = plate
        self.score = score
        self.canvas = canvas
        self.id = canvas.create_oval(20,20,40,40,fill=color)
        self.canvas.move(self.id,230,155)
        numbers = [-3,-2,-1,1,2,3]
        self.x = random.choice(numbers)
        self.y = -2
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()


    def hit_plate(self,position):
        position_plate = self.canvas.coords(self.plate.id)   

        if position[2] >= position_plate[0] and position[0] <= position_plate[2]:
            if position[3] >= position_plate[1] and position[3] <= position_plate[3]:
                self.score.hit()
                return True
        return False        
        


    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        position = self.canvas.coords(self.id)   
        if position[1] <= 0:
            self.y = 2
        elif position[3] >= self.canvas_height:
            self.hit_bottom = True
            self.canvas.create_text(250,250,text='вы проиграли',font=('Courier',25),fill = 'red')

        elif position[0] <= 0:
            self.x = 2
        elif position[2] >= self.canvas_width:
            self.x = -2   
        elif self.hit_plate(position):
            self.y = -10

class Plate:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0,0,150,20,fill=color)
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.move(self.id,self.canvas_width / 2 - 150 / 2,350)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>',self.left)
        self.canvas.bind_all('<KeyPress-Right>',self.right)
    
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        position = self.canvas.coords(self.id)
        if position[2] >= self.canvas_width:
            self.x = 0
        elif position[0] <= 0:
            self.x = 0


    def left(self,event):
        self.x = -2

    def right(self,event):
        self.x = 2
    
class Score:
    def __init__(self,canvas,color):
        self.score = 0
        self.canvas = canvas
        self.text = self.canvas.create_text(10,10,text=self.score,font=('Courier',16),fill = color)
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.text,text=self.score)



plate = Plate(canvas,'blue')
score = Score(canvas,'black')
ball = Ball(canvas,'red',plate,score)
while True:
    if not ball.hit_bottom:
        ball.draw()
        plate.draw()
    else:
        time.sleep(2)
        break
    screen.update_idletasks()
    screen.update()
    time.sleep(.01) 