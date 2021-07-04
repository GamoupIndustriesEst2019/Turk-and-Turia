import pygame as pg, sys

clock = pg.time.Clock()

from pygame.locals import *
pg.init()

pg.display.set_caption("Turk and Turia")

screen = pg.display.set_mode((540, 540))
sky_color = (180, 254, 255)

turk_right = pg.image.load('TurkStand.png')
turk_left = pg.transform.flip(turk_right, True, False)
turk_image = turk_right

exit_box = pg.image.load('ExitBox.png')

turk_x = 50
turk_y = 270
move_left = False
move_right = False
turk_x_momentum = 0
direction = "right"
turk_rect = turk_image.get_rect()
falling_speed = 0

while True:

    grass_rect = pg.draw.rect(screen, (0, 100, 0), pg.Rect((0, 480), (540, 540))

    if turk_rect.colliderect(grass_rect) == True:
        falling_speed = 0
    else:
        falling_speed += 1

    turk_y += falling_speed

    turk_location = (turk_x, turk_y)

    screen.fill(sky_color)
    screen.blit(turk_image,turk_location)
    screen.blit(exit_box,(519,1))

    if move_right == True:
        turk_image = turk_right
        if turk_x_momentum >= 4:
            turk_x_momentum = 4
        else:
            turk_x_momentum += 1
        turk_x += turk_x_momentum
    elif move_left == True:
        turk_image = turk_left
        if turk_x_momentum >= 4:
            turk_x_momentum = 4
        else:
            turk_x_momentum += 1
        turk_x -= turk_x_momentum
    else:
        if turk_x_momentum >= 0:
            turk_x_momentum -= 1
        else:
            turk_x_momentum = 0

    for event in pg.event.get():
        if event.type == QUIT:
            print("Game has been closed.")
            pg.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                move_right = True
            if event.key == K_LEFT:
                move_left = True
            if event.key == K_UP:
                jump = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                move_right = False
            if event.key == K_LEFT:
                move_left = False
            if event.key == K_UP:
                jump = False
            if event.key == K_BACKSPACE:
                print("Game has been closed.")
                pg.quit()
                sys.exit()

    pg.display.update()
    clock.tick(60)
