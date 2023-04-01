from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Доганялки")
backgraund = transform.scale(image.load("background.png"), (700, 500))
window.blit(backgraund, (0, 0))

clock = time.Clock()

class Sprite:


    def __init__(self, image_title, x, y, width=100, height=100):
        self.image = transform.scale(image.load(image_title), (width, height))
        self.x = x
        self.y = y

    def draw_image(self):
        window.blit(self.image, (self.x, self.y))

    def go_up(self):
        self.y -= 10
    
    def go_down(self):
        self.y += 10
    
    def go_left(self):
        self.x -= 10

    def go_right(self):
        self.x += 10        

player1 = Sprite("sprite1.png", 450, 200)
player1.draw_image()

player2 = Sprite("sprite2.png", 50, 200)
player2.draw_image()

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    pressed_keys = key.get_pressed()
    if pressed_keys[K_UP] and player1.y > 0:
        player1.go_up()
    if pressed_keys[K_DOWN] and player1.y < 400:
        player1.go_down()
    if pressed_keys[K_LEFT] and player1.x > 0:
        player1.go_left()
    if pressed_keys[K_RIGHT] and player1.x < 600:
        player1.go_right()

    if pressed_keys[K_w] and player2.y > 0:
        player2.go_up()
    if pressed_keys[K_s] and player2.y < 400:
        player2.go_down()
    if pressed_keys[K_a] and player2.x > 0:
        player2.go_left()
    if pressed_keys[K_d] and player2.x < 600:
        player2.go_right()
    window.blit(backgraund, (0, 0))
    player1.draw_image()
    player2.draw_image()
    display.update()
    clock.tick(60)
