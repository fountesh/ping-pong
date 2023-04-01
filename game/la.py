from pygame import *
from map import make_map
import random
init()
mixer.init()
window = display.set_mode((700, 600))
display.set_caption("Лабіринт")
background = transform.scale(image.load("game/resources/background.jpg"), (700, 600))
window.blit(background, (0, 0))
mixer_music.load("game/resources/jungles.ogg")
mixer_music.play()
kick = mixer.Sound("game/resources/kick.ogg") 
money = mixer.Sound("game/resources/money.ogg")
clock = time.Clock()
game = True


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed=0):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw_sprite(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def is_collide(self, sprite):
        
        return self.rect.colliderect(sprite.rect)


class Player(GameSprite):

    def update(self):
        pressed_keys = key.get_pressed()  
        if pressed_keys[K_w]:
            self.rect.y -= self.speed  
        if pressed_keys[K_s]:
            self.rect.y += self.speed
        if pressed_keys[K_a]:
            self.rect.x -= self.speed  
        if pressed_keys[K_d]:
            self.rect.x += self.speed


class Enemy(GameSprite):

    def update(self, x1, x2):
        if self.rect.x <= x1 or self.rect.x + self.rect.width >= x2:
            self.speed *= -1
        self.rect.x += self.speed


hero = Player('game/resources/hero.png', 0, 0, 5)
hero.draw_sprite()
cyborg = Enemy('game/resources/cyborg.png', 470, 300, 2)
cyborg.draw_sprite()
treasure = GameSprite('game/resources/treasure.png', 580, 480)
treasure.draw_sprite()

game_map = make_map()  

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    hero.update()
    cyborg.update(450, 650)
    if hero.is_collide(cyborg):
        kick.play() 
        game = False
        label = font.SysFont("Algerian", 50).render("You Lose", True, (150, 0, 130))
    if hero.is_collide(treasure):
        money.play()  
        game = False
        label = font.SysFont("Algerian", 50).render("You Win", True, (0, 150, 130))
    window.blit(background, (0, 0))  
    for block in game_map:
        if hero.rect.colliderect(block):
            kick.play()  
            hero.rect.x = 0 
            hero.rect.y = 0
        draw.rect(window, (150, 0, 130), block)
    hero.draw_sprite()
    cyborg.draw_sprite()
    treasure.draw_sprite()
    display.update()
    clock.tick(60)



counter = 0
window.blit(label, (200, 200))
display.update()
game = True
while counter != 5 * 60 and game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    counter += 1
    clock.tick(60)