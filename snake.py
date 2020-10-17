import turtle
import time
import random
import winsound

delay = 0.1
score = 0
high_score = 0

# set up the screen
wn = turtle.Screen()
wn.title("GamAcy")
wn.bgcolor('black')
wn.setup(width=500, height=500)
wn.tracer(0)  # this turns of the screen updates

# snake head
head = turtle.Turtle()  # making a turtle
head.speed(0)  # animation speed
head.shape('square')
head.color('white')
head.penup()  # to not to draw line
head.goto(0, 0)  # start at the center of the screen
head.direction = 'stop'  # in the beginning the turtle is just stopped at the center of the window

# making the snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)

# making the pen for writing text on the window
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('yellow')
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
pen.write("Ready :)", align="center", font=("Courier", 18, "normal"))


# helper functions

def eat_sound():
    winsound.Beep(700, 100)


def collide_win_sound():
    winsound.Beep(1000, 50)
    winsound.Beep(700, 50)
    winsound.Beep(1000, 50)
    winsound.Beep(700, 50)


def pen_print():
    pen.clear()
    pen.goto(0, 230)
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 14, "normal"))


# functions
def go_up():
    if head.direction != 'down':  # if the head is not going down then only up is allowed
        head.direction = 'up'


def go_down():
    if head.direction != 'up':  # if the head is not going up then down is allowed
        head.direction = 'down'


def go_left():
    if head.direction != 'right':  # if the head is not going right, then only left is allowed
        head.direction = 'left'


def go_right():
    if head.direction != 'left':  # if the head is not going left, then only right is allowed
        head.direction = 'right'


def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)


# keyboard bindings
wn.listen()  # window listens for any actions
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')

segments = []       # list for the body segments of the snake

# main game loop
while True:
    wn.update()
    # check if head collides with any of the borders [COLLISION]
    if head.xcor() > 240 or head.xcor() < -240 or head.ycor() > 240 or head.ycor() < -240:
        collide_win_sound()

        head.goto(0, 0)  # making head go again to 0,0
        head.direction = 'stop'
        for seg in segments:  # cleaning the ground
            seg.goto(1000, 1000)
        segments.clear()

        if score > high_score:  # if the score is greater than the high score
            high_score = score
        score = 0  # resetting the score
        pen_print()

        delay = 0.1  # resetting the delay back to original delay



    # check for the collision with the food
    # if the distance between head and the food is less than 20 pixel then move the food to some random position within the window size
    if head.distance(food) < 20:
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        food.goto(x, y)

        # add new_segment to the segments list  (where new_segment is the new object of the turtle class
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)  # appending the new_segment of the snake to the segments list

        eat_sound()

        score += 1
        pen_print()

        delay -= 0.001  # increasing the snake speed by decreasing the program sleep delay


        # moving new_segments in the reverse order to follow it's previous segment
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()      # calling the move function

    # after the move() we want to check if the head collides with its body segments [BODY Collisions]
    for segment in segments:
        if segment.distance(head) < 20:
            collide_win_sound()

            head.goto(0, 0)
            head.direction = 'stop'

            for seg in segments:  # making the segments go out of the screen
                seg.goto(1000, 1000)
            segments.clear()  # clearing the list

            if score > high_score:  # if the score is greater than the high score
                high_score = score
            score = 0  # resetting the score
            pen_print()

            delay = 0.1  # resetting the delay back to original delay

    time.sleep(delay)

wn.mainloop()
