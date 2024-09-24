from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x, y):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.1)

def run_top():
    print('Top')

    for x in range(0, 800, 10):
        draw_boy(x, 550)
        

    pass

def run_right():
    print('Right')

    for y in range(550, 0, -10):
        draw_boy(790, y)

    pass

def run_bottom():
    print('Bottom')

    for x in range(790, 0, -10):
        draw_boy(x, 10)

    pass

def run_left():
    print('OOOOOOOO')

    for y in range(0, 600, 10):
        draw_boy(20, y)

    pass

def run_rectangle():
    print('Rectangle')
    
    run_top()
    run_right()
    run_bottom()
    run_left()
    
    pass

def run_circle():
    print('Circle')

    r, cx, cy = 300, 800 // 2, 600 // 2

    for d in range(0, 360):
    
        x = r * math.cos(math.radians(d)) + cx
        y = r * math.sin(math.radians(d)) + cy

        draw_boy(x, y) 
    pass

def triangle_bottom():
    print('triangle Bottom')

    for x in range(0, 800, 10):
        draw_boy(x, 10)

    pass

def triangle_right():
    print('triangle Right')

    y = 0

    for x in range(800, 400, -10):
        y += 10
        draw_boy(x, y)

    pass

def triangle_left():
    print('triangle Left')

    y = 400
    for x in range(400, 0, -10):
        y -= 10
        draw_boy(x, y)

    pass

def run_triangle():
    
    triangle_bottom()
    triangle_right()
    triangle_left()
    
    pass

while True:
    # run_rectangle()
    # run_circle()
    run_triangle()
    break

close_canvas()
