from pygame import *
init()
width = 1500
height = 700
window = display.set_mode((width, height))
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
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > width:
            self.rect.right = width

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > height:
            self.rect.bottom = height

        pressed_keys = key.get_pressed()
        if pressed_keys[K_w]:
            self.rect.y -= self.speed  
        if pressed_keys[K_s]:
            self.rect.y += self.speed
        if pressed_keys[K_a]:
            self.rect.x -= self.speed
        if pressed_keys[K_d]:
            self.rect.x += self.speed

    def update2(self):
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > width:
            self.rect.right = width

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > height:
            self.rect.bottom = height

        pressed_keys = key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.y -= self.speed
        if pressed_keys[K_DOWN]:
            self.rect.y += self.speed
        if pressed_keys[K_LEFT]:
            self.rect.x -= self.speed
        if pressed_keys[K_RIGHT]:
            self.rect.x += self.speed
speed_x = 5
speed_y = 5
class Ball(GameSprite):
    def muve(self):
        global speed_x
        global speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y    
    #    self.speed.x = self.speed
    #    self.speed.y = self.speed
    #    if finish != True:
    #       self.rect.x += self.speed
    #       self.rect.y += self.speed
                    
        
        
        #self.rect.x += self.speed
        #self.rect.y += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
            speed_x *= -1    
        elif self.rect.right > width:
            self.rect.right = width
            speed_x *= -1

        if self.rect.top < 0:
            self.rect.top = 0
            speed_y *= -1
        elif self.rect.bottom > height:
            self.rect.bottom = height
            speed_y *= -1

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1    
        #if sprite.collide_rect(player1,  ball) or sprite.collide_rect(player2, ball):
        #    self.rect.x -= self.speed 
        
player1 = Player("resurce\player1.png",100, 260, (100, 100), 10)
player2 = Player("resurce\player2.png",1300, 260, (100, 100), 10)
ball = Ball("resurce/ball.png",750, 350, (50, 50), 0)
text1 = font.SysFont("Arial", 50).render("player 1 WIN", True, (0, 150, 130))
text2 = font.SysFont("Arial", 50).render("player2 WIN", True, (0, 150, 130))

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    player1.update1()
    player2.update2()
    ball.muve()   
    window.fill((20, 180, 150))
    player1.draw_sprite()
    player2.draw_sprite()
    ball.draw_sprite()
    if ball.rect.x >=1450:
        window.fill((0, 0, 0))
        window.blit(text1, (750, 350))
        game = False
    elif ball.rect.x <= 0:
        window.fill((0, 0, 0))
        window.blit(text2, (750, 350))
        game = False
    display.update()
    clock.tick(60)