from tkinter import *
import random
import time
window = Tk()
window.title("Wing Dash")
canvas = Canvas(window,width=400,height=600)
canvas.pack()



class Bird:
    def __init__(self,canvas,width,height):
        self.canvas = canvas
        self.width = width
        self.height = height
    def jump(self):
        pass

    def draw(self):
        pass

    def move(self):
        pass

class Pipe:
    def __init__(self,canvas,width,height):
        self.canvas = canvas
        self.width = width
        self.height = height

    def draw(self):
        pass

    def slide(self):
        pass

class Game:
    def __init__(self,canvas,width,height):
        self.canvas = canvas
        self.width = width
        self.height = height

    def draw_background(self):
        self.canvas.create_rectangle(0,0,self.width,self.height,fill="skyblue",outline="")


    def spawn_pipe(self):
        pass

    def check_collision(self):
        pass

    def draw (self):
        self.draw_background()

        pass

    def restart(self):
        pass

    def run_game(self):
        pass

game = Game(canvas,400,600)
game.draw()
window.mainloop()