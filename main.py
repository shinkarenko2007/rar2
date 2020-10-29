import pygame as pg

SIZE = WIDTH, HEIGHT = 800, 600
GRAY = (128, 128, 128)

pg.init()
pg.display.set_caption('Rally')
screen = pg.display.set_mode(SIZE)

FPS = 120
clock = pg.time.Clock()


class Car(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Image/car1.png')


car1 = Car()
car1_image = car1.image
car1_w, car1_h = car1.image.get_width(), car1.image.get_height()
# print(car1_w, car1_h)
car1.x, car1.y = (WIDTH - car1_w) // 2, (HEIGHT - car1_h) // 2

game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False

    car1.y -= 1
    if car1.y < -car1_h:
        car1.y = HEIGHT

    screen.fill(GRAY)
    screen.blit(car1_image, (car1.x, car1.y))
    pg.display.update()
    clock.tick(FPS)
    pg.display.set_caption(f'Rally   FPS: {int(clock.get_fps())}')
