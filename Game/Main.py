import pygame

import random
import math

#from pygame import MOUSEBUTTONDOWN

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# background
background = pygame.image.load('edc.jpg')

#Pictures
picture_one = pygame.image.load("Hard mode/Adventure/a.jpg")
picture_two = pygame.image.load("Hard mode/Adventure/b.jpg")
picture_three = pygame.image.load("Hard mode/Adventure/c.jpg")
picture_four = pygame.image.load("Hard mode/Adventure/d.jpg")
logo = pygame.image.load("logs-removebg-preview.png")
emp = pygame.image.load("sav.jpg")

class Boxes:
    #white boxes
    boxX = [466, 510, 554, 598, 642, 686, 730, 774, 466, 510, 554, 598, 642, 686, 730, 774]
    boxY = [520, 520, 520, 520, 520, 520, 520, 520, 564, 564, 564, 564, 564, 564, 564, 564]
    box = []
    num_of_white_boxes = 16

    for i in range(num_of_white_boxes):
        box.append(pygame.image.load("qaz.jpg"))

    box_rects = [pygame.Rect(x, y, 40, 40) for x, y in zip(boxX, boxY)]

    @staticmethod
    def clicks(mouse_pos):
        for i, rect in enumerate(Boxes.box_rects):
            if rect.collidepoint(mouse_pos):
                print(f"Box {i + 1} clicked!")
                # handle the click event for this box
                return

    #def clicks(a, b, x, y):
    #    dis = math.sqrt((a - (x-40)) ** 2 + (b - (y-40)) ** 2)
    #    return dis <= 40

#Template
#Adventure space
A1 = (442+6, 430+4)
A2 = (486+6, 430+4)
A3 =  (530+6, 430+4)
A4 =  (574+6, 430+4)
A5 =  (618+6, 430+4)
A6=  (662+6, 430+4)
A7 =  (706+6, 430+4)
A8 =  (750+6, 430+4)
A9 =  (794+6, 430+4)

# Top 8 40px
T1 = (466+6, 520+4)
T2 = (510+6, 520+4)
T3 = (554+6, 520+4)
T4 = (598+6, 520+4)
T5 = (642+6, 520+4)
T6 = (686+6, 520+4)
T7 = (730+6, 520+4)
T8 = (774+6, 520+4)

# Bottom 8 40px
B1 = (466+6, 564+4)
B2 = (510+6, 564+4)
B3 = (554+6, 564+4)
B4 = (598+6, 564+4)
B5 = (642+6, 564+4)
B6 = (686+6, 564+4)
B7 = (730+6, 564+4)
B8 = (774+6, 564+4)

#Texts
font = pygame.font.Font('freesansbold.ttf',32)

#textX = 466+6
#textY = 520+4

#random numbers
random_x = random.randrange(466+6, 774+6, 44)
random_y = random.randrange(520+4, 564+4, 44)

ans_one = font.render("A", True, (0, 0, 0))
ans_two = font.render("D", True, (0, 0, 0))
ans_three = font.render("V", True, (0, 0, 0))
ans_four = font.render("E", True, (0, 0, 0))
ans_five = font.render("N", True, (0, 0, 0))
ans_six = font.render("T", True, (0, 0, 0))
ans_seven = font.render("U", True, (0, 0, 0))
ans_eight = font.render("R", True, (0, 0, 0))
ans_nine = font.render("E", True, (0, 0, 0))
others_one = font.render("P", True, (0, 0, 0))
others_two = font.render("E", True, (0, 0, 0))
others_three = font.render("I", True, (0, 0, 0))
others_four = font.render("O", True, (0, 0, 0))
others_five = font.render("H", True, (0, 0, 0))
others_six = font.render("R", True, (0, 0, 0))
others_seven = font.render("S", True, (0, 0, 0))


while running:
    click = False
    mouse_pos = pygame.mouse.get_pos()

    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    # background image
    screen.blit(background, (0, 0))

    # RENDER YOUR GAME HERE

    #Pics
    screen.blit(logo, (1280-150, 720-150))
    screen.blit(picture_one, (488, 98))
    screen.blit(picture_two, (642, 98))
    screen.blit(picture_three, (488, 252))
    screen.blit(picture_four, (642, 252))

    #Question Boxes
    #Adventure Space       -44
    screen.blit(emp, (442, 430))
    screen.blit(emp, (486, 430))
    screen.blit(emp, (530, 430))
    screen.blit(emp, (574, 430))
    screen.blit(emp, (618, 430))
    screen.blit(emp, (662, 430))
    screen.blit(emp, (706, 430))
    screen.blit(emp, (750, 430))
    screen.blit(emp, (794, 430))

    #Top 8 40px            44
    for i, rect in enumerate(zip(Boxes.box_rects)):
        screen.blit(Boxes.box[i], rect)

    #Bottom 8 40px
    # ...

    screen.blit(ans_one, T1)
    screen.blit(ans_two, B6)
    screen.blit(ans_three, T4)
    screen.blit(ans_four, B1)
    screen.blit(ans_five, T5)
    screen.blit(ans_six, B8)
    screen.blit(ans_seven, B2)
    screen.blit(ans_eight, T3)
    screen.blit(ans_nine, T7)
    screen.blit(others_one, B3)
    screen.blit(others_two, T8)
    screen.blit(others_three, B7)
    screen.blit(others_four, T2)
    screen.blit(others_five, T6)
    screen.blit(others_six, B5)
    screen.blit(others_seven, B4)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    if click:
        Boxes.clicks(mouse_pos)

#    if click:
#        for i, (x, y) in enumerate(zip(Boxes.boxX, Boxes.boxY)):
#            if Boxes.clicks(x, y, *mouse_pos):
#                print(f"Box {i+1} clicked!")
                # handle the click event for this box
