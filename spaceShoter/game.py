from pygame import *
from time import time as time_count
from random import randint
init()
mixer.init()
window = display.set_mode((700, 600))
display.set_caption("Шуткер")
background = transform.scale(image.load("resurce/galaxy.jpg"), (700, 600))
window.blit(background, (0, 0))
mixer.music.load("resurce/space.ogg")
mixer_music.set_volume(0.1)
mixer_music.play()
fire = mixer.Sound("resurce/fire.ogg") 
clock = time.Clock()

game = True
bullets = sprite.Group()



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size, player_speed=0):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw_sprite(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

shot_time = time_count()

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
        if pressed_keys[K_SPACE]:
            global shot_time
            if time_count() - shot_time >= 1:
                bullet_x = self.rect.x + 20
                bullet_y = self.rect.y
                new_bullet = Bullet("resurce/bullet.png", bullet_x, bullet_y, (20, 20), 10)
                bullets.add(new_bullet)
                shot_time = time_count()

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        self.draw_sprite()

score = 0

class Enemy(GameSprite):

    def update(self):
        global score
        global life
        self.rect.y += self.speed
        self.draw_sprite()
        if self.rect.y > 600:
            self.kill()
            life -= 1

life = 3
def draw_hearts():
    global life
    x = 50
    for i in range(life):
        heart = Rect(x, 20, 20, 20)
        draw.rect(window, (255, 5, 10), heart)
        x += 30

enemies_group = sprite.Group()

player = Player("resurce/rocket.png",100, 100, (65, 80), 5)
text = font.SysFont("Arial", 50).render("монстри знищені", True, (0, 150, 130))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if len(enemies_group) < 7:
        enemy = Enemy("resurce/ufo.png", randint(0, 600), -100, (80, 50), 1)
        enemies_group.add(enemy)    
    window.blit(background, (0, 0))
    
    text1 = font.SysFont("Arial", 50).render(str(score), True, (150, 0, 0))
    luse = font.SysFont("Arial", 50).render("You luse", True, (255, 10, 15))
    win = font.SysFont("Arial", 50).render("You win", True, (10, 255, 15))
    window.blit(text, (50, 0))
    window.blit(text1, (10, 0))
    player.update()
    player.draw_sprite()
    enemies_group.update()
    draw_hearts()
    sprite.groupcollide(bullets, enemies_group, True, True)
    bullets.update()
    if life <= 0:
        window.blit(luse, (250, 250))
        game = False
    if len(enemies_group) <= 6:
       score += 1
    if score >= 20:
       window.blit(win, (250, 250)) 
       game = False
    display.update()
    clock.tick(60)
    