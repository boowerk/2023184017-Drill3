from pico2d import *

def run_rectangle():
    print('Rectangle')
    pass

def run_circle():
    print('Circle')    
    pass

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

while True:
    run_rectangle()
    run_circle()

close_canvas()
