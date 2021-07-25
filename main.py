import pygame as pg
import math

pg.init()
size = width, height = 500, 500
rad = 200
screen = pg.display.set_mode(size)
points = []

for i in range(1, 361):
    x = int(math.cos(math.radians(i)) * rad) + height // 2
    y = int(math.sin(math.radians(i)) * rad) + height // 2
    points.append((x, y))

step = 0
pause = False
running = True
color = pg.Color('green')
hcolor = color.hsva

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not pause:
            pause = True
        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE and pause:
            pause = False
    if not pause:
        hcolor = ((hcolor[0] + 0.1) % 256, hcolor[1], hcolor[2], hcolor[3])
        screen.fill((0, 0, 0))
        for i in range(360):
            pg.draw.aaline(screen, hcolor, points[i], points[(round(i * step)) % 360])
        pg.draw.circle(screen, hcolor, (width // 2, height // 2), rad, 1)
        pg.display.flip()
        step += 0.01

pg.quit()