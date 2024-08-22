import pygame

import random

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
class Reset:
    def rest(self):
        # Top 8 40px
        Boxes.T1 = (466 + 6, 520 + 4)
        Boxes.T2 = (510 + 6, 520 + 4)
        Boxes.T3 = (554 + 6, 520 + 4)
        Boxes.T4 = (598 + 6, 520 + 4)
        Boxes.T5 = (642 + 6, 520 + 4)
        Boxes.T6 = (686 + 6, 520 + 4)
        Boxes.T7 = (730 + 6, 520 + 4)
        Boxes.T8 = (774 + 6, 520 + 4)

        # Bottom 8 40px
        Boxes.B1 = (466 + 6, 564 + 4)
        Boxes.B2 = (510 + 6, 564 + 4)
        Boxes.B3 = (554 + 6, 564 + 4)
        Boxes.B4 = (598 + 6, 564 + 4)
        Boxes.B5 = (642 + 6, 564 + 4)
        Boxes.B6 = (686 + 6, 564 + 4)
        Boxes.B7 = (730 + 6, 564 + 4)
        Boxes.B8 = (774 + 6, 564 + 4)

class Boxes:
    # Template
    # Adventure space Template
    A1 = (442+6, 430+6)
    A2 = (486 + 6, 430 + 4)
    A3 = (530 + 6, 430 + 4)
    A4 = (574 + 6, 430 + 4)
    A5 = (618 + 6, 430 + 4)
    A6 = (662 + 6, 430 + 4)
    A7 = (706 + 6, 430 + 4)
    A8 = (750 + 6, 430 + 4)
    A9 = (794 + 6, 430 + 4)

    # Top 8 40px
    T1 = (466 + 6, 520 + 4)
    T2 = (510 + 6, 520 + 4)
    T3 = (554 + 6, 520 + 4)
    T4 = (598 + 6, 520 + 4)
    T5 = (642 + 6, 520 + 4)
    T6 = (686 + 6, 520 + 4)
    T7 = (730 + 6, 520 + 4)
    T8 = (774 + 6, 520 + 4)

    # Bottom 8 40px
    B1 = (466 + 6, 564 + 4)
    B2 = (510 + 6, 564 + 4)
    B3 = (554 + 6, 564 + 4)
    B4 = (598 + 6, 564 + 4)
    B5 = (642 + 6, 564 + 4)
    B6 = (686 + 6, 564 + 4)
    B7 = (730 + 6, 564 + 4)
    B8 = (774 + 6, 564 + 4)
    #Text T
    text_X = []
    text_Y = []
    text = []
    num_of_text = 1

    for h in range(num_of_text):
        text.append("A")

    #white boxes
    boxX = [466, 510, 554, 598, 642, 686, 730, 774, 466, 510, 554, 598, 642, 686, 730, 774]
    boxY = [520, 520, 520, 520, 520, 520, 520, 520, 564, 564, 564, 564, 564, 564, 564, 564]
    box = []
    num_of_white_boxes = 16

    for i in range(num_of_white_boxes):
        box.append(pygame.image.load("qaz.jpg"))

    #after black boxes
    black_boxX = [466, 510, 554, 598, 642, 686, 730, 774, 466, 510, 554, 598, 642, 686, 730, 774]
    black_boxY = [520, 520, 520, 520, 520, 520, 520, 520, 564, 564, 564, 564, 564, 564, 564, 564]
    black_box = []
    num_of_black_boxes = 16

    for j in range(num_of_black_boxes):
        black_box.append(pygame.image.load("sav.jpg"))

    #Answer boxes
    answer_boxX = [442, 486, 530, 574, 618, 662, 706, 750, 794]
    answer_boxY = [430, 430, 430, 430, 430, 430, 430, 430, 430]
    answer_box = []
    num_of_answer_boxes = 9

    for k in range(num_of_answer_boxes):
        answer_box.append(pygame.image.load("sav.jpg"))

    box_rects = [pygame.Rect(x, y, 40, 40) for x, y in zip(boxX, boxY)]
    black_box_rects = [pygame.Rect(x, y, 40, 40) for x, y in zip(black_boxX, black_boxY)]
    answer_box_rects = [pygame.Rect(x, y, 40, 40) for x, y in zip(answer_boxX, answer_boxY)]

    movement_positions = {
        0: (442, 430),
        1: (486, 430),
        2: (530, 430),
        3: (574, 430),
        4: (618, 430),
        5: (662, 430),
        6: (706, 430),
        7: (750, 430),
        8: (794, 430),
        # add more positions for other boxes
    }

    back_value = []

    count = 0

    @staticmethod
    def clicks(mouse_pos):
        for i, rect in enumerate(Boxes.box_rects):
            if rect.collidepoint(mouse_pos) and Boxes.count < len(Boxes.movement_positions) and mouse_pos[1] > 490:
                pos = Boxes.movement_positions[Boxes.count]
                Boxes.box_rects[i] = pygame.Rect(*pos, 40, 40)
                Boxes.count += 1
                Boxes.back_value.append(i)
                if Boxes.count == 1:
                    if i == 0:
                        Boxes.T1 = Boxes.A1
                    if i == 1:
                        Boxes.T2 = Boxes.A1
                    if i == 2:
                        Boxes.T3 = Boxes.A1
                    if i == 3:
                        Boxes.T4 = Boxes.A1
                    if i == 4:
                        Boxes.T5 = Boxes.A1
                    if i == 5:
                        Boxes.T6 = Boxes.A1
                    if i == 6:
                        Boxes.T7 = Boxes.A1
                    if i == 7:
                        Boxes.T8 = Boxes.A1
                    if i == 8:
                        Boxes.B1 = Boxes.A1
                    if i == 9:
                        Boxes.B2 = Boxes.A1
                    if i == 10:
                        Boxes.B3 = Boxes.A1
                    if i == 11:
                        Boxes.B4 = Boxes.A1
                    if i == 12:
                        Boxes.B5 = Boxes.A1
                    if i == 13:
                        Boxes.B6 = Boxes.A1
                    if i == 14:
                        Boxes.B7 = Boxes.A1
                    if i == 15:
                        Boxes.B8 = Boxes.A1
                if Boxes.count == 2:
                    if i == 0:
                        Boxes.T1 = Boxes.A2
                    if i == 1:
                        Boxes.T2 = Boxes.A2
                    if i == 2:
                        Boxes.T3 = Boxes.A2
                    if i == 3:
                        Boxes.T4 = Boxes.A2
                    if i == 4:
                        Boxes.T5 = Boxes.A2
                    if i == 5:
                        Boxes.T6 = Boxes.A2
                    if i == 6:
                        Boxes.T7 = Boxes.A2
                    if i == 7:
                        Boxes.T8 = Boxes.A2
                    if i == 8:
                        Boxes.B1 = Boxes.A2
                    if i == 9:
                        Boxes.B2 = Boxes.A2
                    if i == 10:
                        Boxes.B3 = Boxes.A2
                    if i == 11:
                        Boxes.B4 = Boxes.A2
                    if i == 12:
                        Boxes.B5 = Boxes.A2
                    if i == 13:
                        Boxes.B6 = Boxes.A2
                    if i == 14:
                        Boxes.B7 = Boxes.A2
                    if i == 15:
                        Boxes.B8 = Boxes.A2
                if Boxes.count == 3:
                    if i == 0:
                        Boxes.T1 = Boxes.A3
                    if i == 1:
                        Boxes.T2 = Boxes.A3
                    if i == 2:
                        Boxes.T3 = Boxes.A3
                    if i == 3:
                        Boxes.T4 = Boxes.A3
                    if i == 4:
                        Boxes.T5 = Boxes.A3
                    if i == 5:
                        Boxes.T6 = Boxes.A3
                    if i == 6:
                        Boxes.T7 = Boxes.A3
                    if i == 7:
                        Boxes.T8 = Boxes.A3
                    if i == 8:
                        Boxes.B1 = Boxes.A3
                    if i == 9:
                        Boxes.B2 = Boxes.A3
                    if i == 10:
                        Boxes.B3 = Boxes.A3
                    if i == 11:
                        Boxes.B4 = Boxes.A3
                    if i == 12:
                        Boxes.B5 = Boxes.A3
                    if i == 13:
                        Boxes.B6 = Boxes.A3
                    if i == 14:
                        Boxes.B7 = Boxes.A3
                    if i == 15:
                        Boxes.B8 = Boxes.A3
                if Boxes.count == 4:
                    if i == 0:
                        Boxes.T1 = Boxes.A4
                    if i == 1:
                        Boxes.T2 = Boxes.A4
                    if i == 2:
                        Boxes.T3 = Boxes.A4
                    if i == 3:
                        Boxes.T4 = Boxes.A4
                    if i == 4:
                        Boxes.T5 = Boxes.A4
                    if i == 5:
                        Boxes.T6 = Boxes.A4
                    if i == 6:
                        Boxes.T7 = Boxes.A4
                    if i == 7:
                        Boxes.T8 = Boxes.A4
                    if i == 8:
                        Boxes.B1 = Boxes.A4
                    if i == 9:
                        Boxes.B2 = Boxes.A4
                    if i == 10:
                        Boxes.B3 = Boxes.A4
                    if i == 11:
                        Boxes.B4 = Boxes.A4
                    if i == 12:
                        Boxes.B5 = Boxes.A4
                    if i == 13:
                        Boxes.B6 = Boxes.A4
                    if i == 14:
                        Boxes.B7 = Boxes.A4
                    if i == 15:
                        Boxes.B8 = Boxes.A4
                if Boxes.count == 5:
                    if i == 0:
                        Boxes.T1 = Boxes.A5
                    if i == 1:
                        Boxes.T2 = Boxes.A5
                    if i == 2:
                        Boxes.T3 = Boxes.A5
                    if i == 3:
                        Boxes.T4 = Boxes.A5
                    if i == 4:
                        Boxes.T5 = Boxes.A5
                    if i == 5:
                        Boxes.T6 = Boxes.A5
                    if i == 6:
                        Boxes.T7 = Boxes.A5
                    if i == 7:
                        Boxes.T8 = Boxes.A5
                    if i == 8:
                        Boxes.B1 = Boxes.A5
                    if i == 9:
                        Boxes.B2 = Boxes.A5
                    if i == 10:
                        Boxes.B3 = Boxes.A5
                    if i == 11:
                        Boxes.B4 = Boxes.A5
                    if i == 12:
                        Boxes.B5 = Boxes.A5
                    if i == 13:
                        Boxes.B6 = Boxes.A5
                    if i == 14:
                        Boxes.B7 = Boxes.A5
                    if i == 15:
                        Boxes.B8 = Boxes.A5
                if Boxes.count == 6:
                    if i == 0:
                        Boxes.T1 = Boxes.A6
                    if i == 1:
                        Boxes.T2 = Boxes.A6
                    if i == 2:
                        Boxes.T3 = Boxes.A6
                    if i == 3:
                        Boxes.T4 = Boxes.A6
                    if i == 4:
                        Boxes.T5 = Boxes.A6
                    if i == 5:
                        Boxes.T6 = Boxes.A6
                    if i == 6:
                        Boxes.T7 = Boxes.A6
                    if i == 7:
                        Boxes.T8 = Boxes.A6
                    if i == 8:
                        Boxes.B1 = Boxes.A6
                    if i == 9:
                        Boxes.B2 = Boxes.A6
                    if i == 10:
                        Boxes.B3 = Boxes.A6
                    if i == 11:
                        Boxes.B4 = Boxes.A6
                    if i == 12:
                        Boxes.B5 = Boxes.A6
                    if i == 13:
                        Boxes.B6 = Boxes.A6
                    if i == 14:
                        Boxes.B7 = Boxes.A6
                    if i == 15:
                        Boxes.B8 = Boxes.A6
                if Boxes.count == 7:
                    if i == 0:
                        Boxes.T1 = Boxes.A7
                    if i == 1:
                        Boxes.T2 = Boxes.A7
                    if i == 2:
                        Boxes.T3 = Boxes.A7
                    if i == 3:
                        Boxes.T4 = Boxes.A7
                    if i == 4:
                        Boxes.T5 = Boxes.A7
                    if i == 5:
                        Boxes.T6 = Boxes.A7
                    if i == 6:
                        Boxes.T7 = Boxes.A7
                    if i == 7:
                        Boxes.T8 = Boxes.A7
                    if i == 8:
                        Boxes.B1 = Boxes.A7
                    if i == 9:
                        Boxes.B2 = Boxes.A7
                    if i == 10:
                        Boxes.B3 = Boxes.A7
                    if i == 11:
                        Boxes.B4 = Boxes.A7
                    if i == 12:
                        Boxes.B5 = Boxes.A7
                    if i == 13:
                        Boxes.B6 = Boxes.A7
                    if i == 14:
                        Boxes.B7 = Boxes.A7
                    if i == 15:
                        Boxes.B8 = Boxes.A7
                if Boxes.count == 8:
                    if i == 0:
                        Boxes.T1 = Boxes.A8
                    if i == 1:
                        Boxes.T2 = Boxes.A8
                    if i == 2:
                        Boxes.T3 = Boxes.A8
                    if i == 3:
                        Boxes.T4 = Boxes.A8
                    if i == 4:
                        Boxes.T5 = Boxes.A8
                    if i == 5:
                        Boxes.T6 = Boxes.A8
                    if i == 6:
                        Boxes.T7 = Boxes.A8
                    if i == 7:
                        Boxes.T8 = Boxes.A8
                    if i == 8:
                        Boxes.B1 = Boxes.A8
                    if i == 9:
                        Boxes.B2 = Boxes.A8
                    if i == 10:
                        Boxes.B3 = Boxes.A8
                    if i == 11:
                        Boxes.B4 = Boxes.A8
                    if i == 12:
                        Boxes.B5 = Boxes.A8
                    if i == 13:
                        Boxes.B6 = Boxes.A8
                    if i == 14:
                        Boxes.B7 = Boxes.A8
                    if i == 15:
                        Boxes.B8 = Boxes.A8
                if Boxes.count == 9:
                    if i == 0:
                        Boxes.T1 = Boxes.A9
                    if i == 1:
                        Boxes.T2 = Boxes.A9
                    if i == 2:
                        Boxes.T3 = Boxes.A9
                    if i == 3:
                        Boxes.T4 = Boxes.A9
                    if i == 4:
                        Boxes.T5 = Boxes.A9
                    if i == 5:
                        Boxes.T6 = Boxes.A9
                    if i == 6:
                        Boxes.T7 = Boxes.A9
                    if i == 7:
                        Boxes.T8 = Boxes.A9
                    if i == 8:
                        Boxes.B1 = Boxes.A9
                    if i == 9:
                        Boxes.B2 = Boxes.A9
                    if i == 10:
                        Boxes.B3 = Boxes.A9
                    if i == 11:
                        Boxes.B4 = Boxes.A9
                    if i == 12:
                        Boxes.B5 = Boxes.A9
                    if i == 13:
                        Boxes.B6 = Boxes.A9
                    if i == 14:
                        Boxes.B7 = Boxes.A9
                    if i == 15:
                        Boxes.B8 = Boxes.A9
                    if (Boxes.T1 == Boxes.A1 and Boxes.B6 == Boxes.A2 and Boxes.T4 == Boxes.A3 and
                            (Boxes.T7 == Boxes.A4 or Boxes.T8 == Boxes.A4 or Boxes.B1 == Boxes.A4) and
                                Boxes.T5 == Boxes.A5 and Boxes.B8 == Boxes.A6 and Boxes.B2 == Boxes.A7 and
                                    Boxes.T3 == Boxes.A8 and (Boxes.T7 == Boxes.A9 or Boxes.T8 == Boxes.A9 or
                                                            Boxes.B1 == Boxes.A9)):
                        print("Winner")
                    else:
                        print("Loser")
                        Reset.rest()
                return

#    def back(mouse_pos):
#        for i, rect in enumerate(Boxes.box_rects):
#            if rect.collidepoint(mouse_pos) and Boxes.count == len(Boxes.back_value):
#                post = Boxes.back_value[Boxes.count]
#                Boxes.box_rects[i] = pygame.Rect(*post, 40, 40)
#                Boxes.count -= 1
#                print(Boxes.count)
#                return

#Texts
font = pygame.font.Font('freesansbold.ttf',32)

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
            Boxes.clicks(mouse_pos)  # call the clicks method here

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


    #Top 8 40px            44
    for k, rect in enumerate(zip(Boxes.answer_box_rects)):
        screen.blit(Boxes.answer_box[k], rect)

    for j, rect in enumerate(zip(Boxes.black_box_rects)):
        screen.blit(Boxes.black_box[j], rect)

    for i, rect in enumerate(zip(Boxes.box_rects)):
        screen.blit(Boxes.box[i], rect)

    screen.blit(ans_one, Boxes.T1)
    screen.blit(ans_two, Boxes.B6)
    screen.blit(ans_three, Boxes.T4)
    screen.blit(ans_four, Boxes.B1)
    screen.blit(ans_five, Boxes.T5)
    screen.blit(ans_six, Boxes.B8)
    screen.blit(ans_seven, Boxes.B2)
    screen.blit(ans_eight, Boxes.T3)
    screen.blit(ans_nine, Boxes.T7)
    screen.blit(others_one, Boxes.B3)
    screen.blit(others_two, Boxes.T8)
    screen.blit(others_three, Boxes.B7)
    screen.blit(others_four, Boxes.T2)
    screen.blit(others_five, Boxes.T6)
    screen.blit(others_six, Boxes.B5)
    screen.blit(others_seven, Boxes.B4)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    if click:
        Boxes.clicks(mouse_pos)
