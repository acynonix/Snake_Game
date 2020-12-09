import turtle
import time

win = turtle.Screen()
win.title("Learning Turtle module")
win.bgcolor("white")
win.setup(width=500, height=500)
win.tracer(0)


acy = turtle.Turtle()
acy.shape("turtle")
acy.color("green")
acy.direction = 'stop'
acy.speed(0)
def move():
    if acy.direction == 'up':
        y = acy.ycor()
        acy.sety(y+10)
    if acy.direction == 'down':
        y = acy.ycor()
        acy.sety(y-10)
    if acy.direction == 'left':
        x = acy.xcor()
        acy.setx(x-10)
    if acy.direction == 'right':
        x = acy.xcor()
        acy.setx(x+10)

def go_up():
    acy.direction == 'up'
def go_down():
    acy.direction == 'down'
def go_left():
    acy.direction == 'left'
def go_right():
    acy.direction == 'right'


win.listen()
win.onkeypress(go_up, 'w')
win.onkeypress(go_down, 's')
win.onkeypress(go_left, 'a')
win.onkeypress(go_right, 'd')

while True:
    win.update()
    time.sleep(0.1)
    move()

win.mainloop()