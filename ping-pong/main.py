from pygame import *

window = display.set_mode((500, 500))

clock = time.Clock()

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)