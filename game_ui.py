import pygame
from coin_manager import CoinManager

from games.Easy1 import Game as Easy1
from games.Easy2 import Game as Easy2
from games.Easy3 import Game as Easy3
from games.Easy4 import Game as Easy4
from games.Easy5 import Game as Easy5
from games.Medium1 import Game as Medium1
from games.Medium2 import Game as Medium2
from games.Medium3 import Game as Medium3
from games.Medium4 import Game as Medium4
from games.Medium5 import Game as Medium5
from games.Hard1 import Game as Hard1
from games.Hard2 import Game as Hard2
from games.Hard3 import Game as Hard3
from games.Hard4 import Game as Hard4
from games.Hard5 import Game as Hard5




class GameUI:
    def __init__(self, screen, mode):
        self.screen = screen
        self.mode = mode  # Could be 'easy', 'medium', or 'hard'
        self.width, self.height = self.screen.get_size()
        self.clock = pygame.time.Clock()
        #self.hint_button = pygame.Rect(50, 50, 100, 40)  # Position and size of hint button

        self.bg = pygame.image.load("t1.png")
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.back_button_pressed = False
        self.back_arrow_rect = pygame.Rect(20, 20, 50, 50)

        # Colors
        self.panel_color = (255, 235, 153)  # Light yellow
        self.panel_border_color = (255, 153, 153)  # Pink border
        self.button_color = (255, 255, 255)  # White buttons
        self.button_text_color = (0, 0, 0)  # Black text on buttons
        self.title_text_color = (255, 255, 255)  # White text for title
        self.shadow_color = (50, 50, 50)  # Shadow color

        # Fonts
        self.font = pygame.font.Font(None, 50)
        self.title_font = pygame.font.Font(None, 60)

        # Load a back arrow image or draw it
        self.back_arrow_rect = pygame.Rect(20, 20, 50, 50)  # Position and size for the back arrow

        # UI Elements
        self.panel_rect = pygame.Rect(self.width // 4, self.height // 3, self.width * 2 // 4, self.height // 3)
        self.title_rect = pygame.Rect(self.width // 4, self.height // 4 + 10, self.width // 3, 50)
        self.buttons = []

        # Create buttons with adjusted spacing
        button_width = 60
        button_height = 60
        button_spacing = 20  # Adjusted spacing
        start_x = self.panel_rect.x + (self.panel_rect.width - (5 * button_width + 4 * button_spacing)) // 2
        start_y = self.panel_rect.y + (self.panel_rect.height // 2) - (button_height // 2)

        for i in range(5):
            button_rect = pygame.Rect(
                start_x + i * (button_width + button_spacing),
                start_y,
                button_width,
                button_height
            )
            self.buttons.append(button_rect)

        self.games = {
            "EASY": [Easy1, Easy2, Easy3, Easy4, Easy5],
            "MEDIUM": [Medium1, Medium2, Medium3, Medium4, Medium5],
            "HARD": [Hard1, Hard2, Hard3, Hard4, Hard5]

        }

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if self.back_arrow_rect.collidepoint(mouse_pos):
                print("Back button clicked")
                self.back_button_pressed = True  # Set the flag when the back button is pressed
                return True

            for i, button_rect in enumerate(self.buttons):
                if button_rect.collidepoint(mouse_pos):
                    print(f"Game {i + 1} selected in {self.mode.capitalize()} mode.")
                    game_class = self.games[self.mode][i]  # Select the correct game class
                    game_instance = game_class(self.screen)  # Initialize the game
                    game_instance.run()  # Run the selected game

                    # Move to the selected game (this would typically involve changing states or scenes)

        return False

    def use_hint(self):
        if CoinManager.use_coins(10):  # Deduct coins using CoinManager
            # Logic to reveal a letter in the word
            # You'll need to modify your game logic to accommodate this
            print("Hint used!")  # For debugging
        else:
            print("Not enough coins!")  # For debugging

    def update(self):
        # Add any update logic for the Boxes instance
        pass

    def go_back(self):
        if self.back_button_pressed:
            print("Going back to the home page...")
            self.back_button_pressed = False  # Reset the flag
            return True
        return False

    def draw(self):

        self.screen.blit(self.bg, (0, 0))

        # Draw the back arrow
        arrow_color = (255, 255, 255)  # White arrow
        arrow_points = [
            (self.back_arrow_rect.left + self.back_arrow_rect.width // 3, self.back_arrow_rect.centery),
            (self.back_arrow_rect.right - self.back_arrow_rect.width // 3, self.back_arrow_rect.top),
            (self.back_arrow_rect.right - self.back_arrow_rect.width // 3, self.back_arrow_rect.bottom)
        ]
        pygame.draw.polygon(self.screen, arrow_color, arrow_points)

        self.draw_coin_counter()

        # Draw panel
        pygame.draw.rect(self.screen, self.panel_border_color, self.panel_rect, border_radius=20)
        pygame.draw.rect(self.screen, self.panel_color, self.panel_rect.inflate(-20, -20), border_radius=20)

        # Draw title with shadow
        title_text = self.title_font.render("SELECT GAME", True, self.title_text_color)
        title_shadow = self.title_font.render("SELECT GAME", True, self.shadow_color)
        self.screen.blit(title_shadow, (self.title_rect.x + 2, self.title_rect.y + 2))
        self.screen.blit(title_text, (self.title_rect.x, self.title_rect.y))

        # Draw buttons
        for i, button_rect in enumerate(self.buttons):
            pygame.draw.rect(self.screen, self.button_color, button_rect, border_radius=15)
            button_text = self.font.render(str(i + 1), True, self.button_text_color)
            text_rect = button_text.get_rect(center=button_rect.center)
            self.screen.blit(button_text, text_rect)

        pygame.display.flip()
        self.clock.tick(60)

    def draw_coin_counter(self):
        # Display coins from CoinManager
        pygame.draw.rect(self.screen, (255, 192, 203), (self.width - 130, 20, 110, 40), border_radius=20)
        pygame.draw.circle(self.screen, (255, 255, 0), (self.width - 110, 40), 15)
        pygame.draw.circle(self.screen, (0, 0, 0), (self.width - 110, 40), 15, 2)
        coin_text = pygame.font.Font(None, 36).render(str(CoinManager.get_coins()), True, (255, 255, 255))
        coin_rect = coin_text.get_rect(center=(self.width - 60, 40))
        self.screen.blit(coin_text, coin_rect)
