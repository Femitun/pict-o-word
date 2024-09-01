import pygame
import os
from coin_manager import CoinManager


class Reset:
    @staticmethod
    def reset_boxes(boxes):
        boxes.count = 0
        boxes.back_value = []
        boxes.tries_left = 3

        # Reset the box positions
        boxes.box_rects = [pygame.Rect(x, y, 40, 40) for x, y in zip(boxes.boxX, boxes.boxY)]
        boxes.letter_positions = boxes.box_rects[:]

    @staticmethod
    def reset_game(game):
        game.boxes = Boxes()  # Reinitialize the boxes
        game.run()  # Restart the game loop


class Boxes:
    def __init__(self, game):
        self.A2 = (486 + 6, 430 + 4)
        self.A3 = (530 + 6, 430 + 4)
        self.A4 = (574 + 6, 430 + 4)
        self.A5 = (618 + 6, 430 + 4)
        self.A6 = (662 + 6, 430 + 4)
        self.A7 = (706 + 6, 430 + 4)

        self.T1 = (466 + 6, 520 + 4)
        self.T2 = (510 + 6, 520 + 4)
        self.T3 = (554 + 6, 520 + 4)
        self.T4 = (598 + 6, 520 + 4)
        self.T5 = (642 + 6, 520 + 4)
        self.T6 = (686 + 6, 520 + 4)
        self.T7 = (730 + 6, 520 + 4)
        self.T8 = (774 + 6, 520 + 4)

        self.B1 = (466 + 6, 564 + 4)
        self.B2 = (510 + 6, 564 + 4)
        self.B3 = (554 + 6, 564 + 4)
        self.B4 = (598 + 6, 564 + 4)
        self.B5 = (642 + 6, 564 + 4)
        self.B6 = (686 + 6, 564 + 4)
        self.B7 = (730 + 6, 564 + 4)
        self.B8 = (774 + 6, 564 + 4)

        self.boxX = [466, 510, 554, 598, 642, 686, 730, 774, 466, 510, 554, 598, 642, 686, 730, 774]
        self.boxY = [520, 520, 520, 520, 520, 520, 520, 520, 564, 564, 564, 564, 564, 564, 564, 564]
        self.box = [pygame.image.load("qaz.jpg") for _ in range(16)]

        self.black_boxX = [466, 510, 554, 598, 642, 686, 730, 774, 466, 510, 554, 598, 642, 686, 730, 774]
        self.black_boxY = [520, 520, 520, 520, 520, 520, 520, 520, 564, 564, 564, 564, 564, 564, 564, 564]
        self.black_box = [pygame.image.load("sav.jpg") for _ in range(16)]

        self.answer_boxX = [486+22, 530+22, 574+22, 618+22, 662+22, 706+22]
        self.answer_boxY = [430, 430, 430, 430, 430, 430]
        self.answer_box = [pygame.image.load("sav.jpg") for _ in range(6)]

        self.box_rects = [pygame.Rect(x, y, 40, 40) for x, y in zip(self.boxX, self.boxY)]
        self.black_box_rects = [pygame.Rect(x, y, 40, 40) for x, y in zip(self.black_boxX, self.black_boxY)]
        self.answer_box_rects = [pygame.Rect(x, y, 40, 40) for x, y in zip(self.answer_boxX, self.answer_boxY)]

        self.letter_positions = self.box_rects[:]

        self.movement_positions = {
            0: (486+22, 430),
            1: (530+22, 430),
            2: (574+22, 430),
            3: (618+22, 430),
            4: (662+22, 430),
            5: (706+22, 430),
        }

        self.correct_positions = {
            0: 2,  # index of the first correct letter
            1: 9,  # index of the second correct letter
            2: 13,  # index of the third correct letter
            3: 8,  # index of the fourth correct letter
            4: 12,  # index of the fifth correct letter
            5: 0,
        }

        self.game = game
        self.hint_button = pygame.Rect(100, 550, 250, 50)  # Example position and size
        self.hint_button_color = (125, 50, 50)  # Example background color (DodgerBlue)
        self.hint_text_color = (255, 255, 255)  # White text color
        self.hint_font = pygame.font.Font(None, 36)

        self.back_value = []
        self.count = 0
        self.tries_left = 3

    def use_hint(self):
        if CoinManager.use_coins(10):  # Deduct 10 coins for a hint
            self.reveal_letter()  # Reveal a letter
            self.display_message("Hint used!", (50, 600), (0, 255, 0))  # Green text for success
            return True
        else:
            self.display_message("Not enough coins!", (50, 600), (255, 0, 0))  # Red text for error
            return False

    def display_message(self, message, position, color):
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, color)
        self.game.screen.blit(text, position)
        pygame.display.flip()
        pygame.time.wait(500)  # Wait for a second to show the message

    def reveal_letter(self):
        for i in range(len(self.movement_positions)):
            if i >= self.count:
                correct_box_index = self.correct_positions[i]
                pos = self.movement_positions[i]
                self.box_rects[correct_box_index] = pygame.Rect(*pos, 40, 40)
                self.letter_positions[correct_box_index] = pygame.Rect(*pos, 40, 40)
                self.count += 1
                self.back_value.append(correct_box_index)
                break

    def check_win(self):
        print("Checking win")
        correct_positions = [(486+22, 430), (530+22, 430), (574+22, 430), (618+22, 430), (662+22, 430), (706+22, 430)]

        #desired_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        current_positions = [self.box_rects[self.correct_positions[i]].topleft for i in range(len(correct_positions))]

        # Return whether the current positions match the expected correct positions
        return current_positions == correct_positions

    def display_win_message(self):
        font = pygame.font.Font(None, 74)
        text = font.render('You Win!', True, (0, 255, 0))
        self.game.screen.blit(text, (540, 360))
        pygame.display.flip()
        pygame.time.wait(2000)
        CoinManager.add_coins(5)  # Reward 20 coins after winning
        self.game.running = False  # Stop the game loop

    def display_lose_message(self):
        font = pygame.font.Font(None, 74)
        text = font.render('YOU LOSE!', True, (255, 0, 0))
        self.game.screen.blit(text, (540, 360))
        pygame.display.flip()
        pygame.time.wait(2000)
        self.game.running = False  # Stop the game loop


    def display_losebuttry_message1(self):
        font = pygame.font.Font(None, 74)
        text = font.render('2 more tries', True, (255,100,0))
        self.game.screen.blit(text, (540, 360))
        pygame.display.flip()
        pygame.time.wait(2000)

    def display_losebuttry_message2(self):
        font = pygame.font.Font(None, 74)
        text = font.render('1 more try', True, (255,20,0))
        self.game.screen.blit(text, (540, 360))
        pygame.display.flip()
        pygame.time.wait(2000)

    def draw_hint_button(self, screen):
        pygame.draw.rect(screen, self.hint_button_color, self.hint_button)
        hint_text = self.hint_font.render("Use Hint (-10 Coins)", True, self.hint_text_color)
        screen.blit(hint_text, (self.hint_button.x + 10, self.hint_button.y + 10))

    def clicks(self, mouse_pos):
        for i, rect in enumerate(self.box_rects):
            if rect.collidepoint(mouse_pos) and self.count < len(self.movement_positions) and mouse_pos[1] > 490:
                pos = self.movement_positions[self.count]
                self.box_rects[i] = pygame.Rect(*pos, 40, 40)
                self.letter_positions[i] = pygame.Rect(*pos, 40, 40)  # Update letter position
                self.count += 1
                self.back_value.append(i)

                # Check if all answer slots are filled
                if self.count == len(self.movement_positions):
                    if self.check_win():
                        print("Winner")
                        self.display_win_message()
                        # pygame.quit() Don't know what to put here to make it go back to game UI yet!

                    else:
                        self.tries_left -= 1
                        if self.tries_left <= 0:
                            pygame.time.wait(200)
                            print("You lose")
                            self.display_lose_message()
                            # pygame.quit() Don't know what to put here to make it go back to game UI yet!
                        else:
                            if self.tries_left == 1:
                                pygame.time.wait(200)
                                print("2 tries")
                                self.display_losebuttry_message2()
                            else:
                                pygame.time.wait(200)
                                print("1 try")
                                self.display_losebuttry_message1()
                return

    def back_click(self, mouse_pos):
        if self.count > 0:
            last_index = self.back_value.pop()
            self.box_rects[last_index] = pygame.Rect(self.boxX[last_index], self.boxY[last_index], 40, 40)
            self.letter_positions[last_index] = pygame.Rect(self.boxX[last_index], self.boxY[last_index], 40, 40)  # Update letter position
            self.count -= 1


class Game:
    def __init__(self, screen):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.boxes = Boxes(self)
        base_path = os.path.dirname(__file__)
        image_path1 = os.path.join(base_path, "hard", "Pastry", "a.png")
        image_path2 = os.path.join(base_path, "hard", "Pastry", "b.png")
        image_path3 = os.path.join(base_path, "hard", "Pastry", "c.png")
        image_path4 = os.path.join(base_path, "hard", "Pastry", "d.png")
        self.hint_font = pygame.font.Font('freesansbold.ttf', 24)
        self.coin_font = pygame.font.Font('freesansbold.ttf', 24)

        self.background = pygame.image.load('edc.jpg')
        self.logo = pygame.image.load("logs-removebg-preview.png")
        self.picture_one = pygame.image.load(image_path1)
        self.picture_two = pygame.image.load(image_path2)
        self.picture_three = pygame.image.load(image_path3)
        self.picture_four = pygame.image.load(image_path4)

        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.ans_one = self.font.render("Y", True, (0, 0, 0))
        self.ans_two = self.font.render("L", True, (0, 0, 0))
        self.ans_three = self.font.render("P", True, (0, 0, 0))
        self.ans_four = self.font.render("C", True, (0, 0, 0))
        self.ans_five = self.font.render("H", True, (0, 0, 0))
        self.ans_six = self.font.render("M", True, (0, 0, 0))
        self.ans_seven = self.font.render("I", True, (0, 0, 0))
        self.ans_eight = self.font.render("N", True, (0, 0, 0))
        self.ans_nine = self.font.render("T", True, (0, 0, 0))

        self.others_one = self.font.render("A", True, (0, 0, 0))
        self.others_two = self.font.render("H", True, (0, 0, 0))
        self.others_three = self.font.render("O", True, (0, 0, 0))
        self.others_four = self.font.render("R", True, (0, 0, 0))
        self.others_five = self.font.render("S", True, (0, 0, 0))
        self.others_six = self.font.render("C", True, (0, 0, 0))
        self.others_seven = self.font.render("B", True, (0, 0, 0))

        self.boxes = Boxes(self)

    def run(self):
        while self.running:
            self.screen.fill("purple")
            self.screen.blit(self.background, (0, 0))

            click = False
            back_click = False
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        if self.boxes.hint_button.collidepoint(mouse_pos):
                            if self.boxes.use_hint():
                                print("Hint used!")
                            else:
                                print("Not enough coins for hint!")
                        else:
                            click = True

                    elif event.button == 3:  # Right click
                        back_click = True

            if click:
                self.boxes.clicks(mouse_pos)
            if back_click:
                self.boxes.back_click(mouse_pos)

            # Display elements
            self.display_elements()

            pygame.display.flip()
            self.clock.tick(60)

    def display_elements(self):
        self.screen.blit(self.logo, (1280 - 150, 720 - 150))
        self.screen.blit(self.picture_one, (488, 98))
        self.screen.blit(self.picture_two, (642, 98))
        self.screen.blit(self.picture_three, (488, 252))
        self.screen.blit(self.picture_four, (642, 252))

        pygame.draw.rect(self.screen, (0, 255, 0), self.boxes.hint_button)
        hint_text = self.hint_font.render("Hint (10)", True, (255, 255, 255))
        hint_rect = hint_text.get_rect(center=self.boxes.hint_button.center)
        self.screen.blit(hint_text, hint_rect)

        for k, rect in enumerate(self.boxes.answer_box_rects):
            self.screen.blit(self.boxes.answer_box[k], rect)

        self.boxes.draw_hint_button(self.screen)


        for j, rect in enumerate(self.boxes.black_box_rects):
            self.screen.blit(self.boxes.black_box[j], rect)

        for i, rect in enumerate(self.boxes.box_rects):
            self.screen.blit(self.boxes.box[i], rect)
            # Display the letters on top of boxes
            if i < 9:
                letter_surface, letter_rect = self.get_answer_letter(i)
                self.screen.blit(letter_surface, letter_rect)
            else:
                letter_surface, letter_rect = self.get_other_letter(i - 9)
                self.screen.blit(letter_surface, letter_rect)

    def get_answer_letter(self, index):
        answer_texts = [
            self.ans_one, self.ans_two, self.ans_three,
            self.ans_four, self.ans_five, self.ans_six,
            self.ans_seven, self.ans_eight, self.ans_nine
        ]
        letter_rect = answer_texts[index].get_rect(center=self.boxes.letter_positions[index].center)
        return answer_texts[index], letter_rect

    def get_other_letter(self, index):
        other_texts = [
            self.others_one, self.others_two, self.others_three,
            self.others_four, self.others_five, self.others_six,
            self.others_seven
        ]
        letter_rect = other_texts[index].get_rect(center=self.boxes.letter_positions[index + 9].center)
        return other_texts[index], letter_rect

if __name__ == "__main__":
    game = Game()
    game.run()