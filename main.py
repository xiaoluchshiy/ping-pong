import pygame.sprite
from pygame import *


class Spritik(sprite.Sprite):
    def __init__(self, s_image, x, y, speed, weight, high):
        super().__init__()
        self.image = transform.scale(image.load(s_image), (weight, high))

        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Spritik):
    def move_left(self):
        pressed_keys = key.get_pressed()

        if pressed_keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if pressed_keys[K_s] and self.rect.y < 615:
            self.rect.y += self.speed

    def move_right(self):
        pressed_keys = key.get_pressed()

        if pressed_keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if pressed_keys[K_DOWN] and self.rect.y < 615:
            self.rect.y += self.speed


class Ball(Spritik):
    def __init__(self, s_image, x, y, speed_x, speed_y, weight, high):
        super().__init__(s_image=s_image, x=x, y=y, speed=0, weight=weight, high=high)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self, player1, plater2):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y <= 5 or self.rect.y >= 665:
            self.speed_y = -self.speed_y
        if sprite.collide_rect(player1, self) or sprite.collide_rect(plater2, self):
            self.speed_x = -self.speed_x


window = display.set_mode((1280, 720))
display.set_caption('пинг-понг')

background = transform.scale(image.load('new_year_background.jpg'), (1280, 720))

left_l = Player('platform.png', 10, 310, 5, 30, 100)
right_r = Player('platform.png', 1240, 310, 5, 30, 100)
ball = Ball('ball.png', 590, 260, 5, 5, 50, 50)

clock = time.Clock()
game = 1
finish = False
font.init()
font1 = font.SysFont('Arial', 50)
loose_l = font1.render('left player loose!', True, (0, 255, 180))
loose_r = font1.render('right player loose!', True, (0, 255, 180))


while game:
    for i in event.get():
        if i.type == QUIT:
            game = 0
    if not finish:
        window.blit(background, (0, 0))

        left_l.reset()
        left_l.move_left()

        right_r.reset()
        right_r.move_right()

        ball.reset()
        ball.move(left_l, right_r)

        if ball.rect.x >= 1230:
            finish = True
            window.blit(loose_r, (500, 320))

        if ball.rect.x <= 0:
            finish = True
            window.blit(loose_l, (500, 320))

    clock.tick(60)
    display.update()
