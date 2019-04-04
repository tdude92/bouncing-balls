from tkinter import *
from random import randint
from time import sleep
from math import sin, cos, radians

root = Tk()

canvas = Canvas(root, width = 400, height = 400, bg = "black")
canvas.pack()

balls = []

for _ in range(20):
    balls.append([canvas.create_oval(195, 195, 205, 205, fill = "red"), randint(0, 360)])

while True:
    for ball in balls:
        if canvas.coords(ball[0])[0] <= 0 and canvas.coords(ball[0])[1] <= 0:
            ball[1] = 315
        elif canvas.coords(ball[0])[0] <= 0 and canvas.coords(ball[0])[3] >= 400:
            ball[1] = 45
        elif canvas.coords(ball[0])[2] >= 400 and canvas.coords(ball[0])[1] <= 0:
            ball[1] = 225
        elif canvas.coords(ball[0])[2] >= 400 and canvas.coords(ball[0])[3] >= 400:
            ball[1] = 135
        elif canvas.coords(ball[0])[0] <= 0:
            angle_reflection = abs(180 - ball[1])
            if ball[1] < 180:
                ball[1] = angle_reflection
            elif ball[1] > 180:
                ball[1] = 360 - angle_reflection
            else:
                ball[1] = 0
        elif canvas.coords(ball[0])[2] >= 400: # Width of canvas.
            if ball[1] < 90:
                ball[1] = 180 - ball[1]
            elif ball[1] > 270:
                ball[1] = 540 - ball[1]
            elif ball[1] == 0:
                ball[1] = 180
        elif canvas.coords(ball[0])[1] <= 0:
            if ball[1] == 90:
                ball[1] = 270
            else:
                ball[1] = 360 - ball[1]
        elif canvas.coords(ball[0])[3] >= 400: # Height of canvas.
            if ball[1] == 270:
                ball[1] = 90
            else:
                ball[1] = 360 - ball[1]
        x_displacement = 100 * cos(radians(ball[1]))
        y_displacement = 100 * sin(radians(ball[1]))

        canvas.move(ball[0], x_displacement / 5, -(y_displacement / 5))
    canvas.update()
    sleep(0.1)

root.mainloop()
