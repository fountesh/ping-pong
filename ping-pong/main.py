from pygame import *
window = display.set_mode((1000, 700))
window.fill((20, 180, 150))
display.set_caption("ping-pong")


clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size, player_speed=0):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        if reversed == False:
            self.image = transform.flip(self.image ,True, False)
    def draw_sprite(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    
    def update1(self):
        pressed_keys = key.get_pressed()
        if pressed_keys[K_w]:
            self.rect.y -= self.speed  
        if pressed_keys[K_s]:
            self.rect.y += self.speed

    def update2(self):
        pressed_keys = key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.y -= self.speed
        if pressed_keys[K_DOWN]:
            self.rect.y += self.speed


player1 = Player("resurce\player1.png",100, 200, (100, 100), 10)
player2 = Player("resurce\player2.png",800, 200, (100, 100), 10)
ball = GameSprite("resurce/ball.png",475, 225, (50, 50))

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    player1.update1()
    player2.update2()
    window.fill((20, 180, 150))
    player1.draw_sprite()
    player2.draw_sprite()
    ball.draw_sprite()
    display.update()
    clock.tick(60)