import pygame

class GameUI:
    def __init__(self, screen, mode):
        self.screen = screen
        self.mode = mode  # Could be 'easy', 'medium', or 'hard'
        self.width, self.height = self.screen.get_size()
        self.clock = pygame.time.Clock()

        self.bg = pygame.image.load("t1.png")
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

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
        self.panel_rect = pygame.Rect(self.width // 6, self.height // 4, self.width * 2 // 3, self.height // 2)
        self.title_rect = pygame.Rect(self.width // 3, self.height // 4 - 40, self.width // 3, 50)
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

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if self.back_arrow_rect.collidepoint(mouse_pos):
                self.go_back()

            for i, button_rect in enumerate(self.buttons):
                if button_rect.collidepoint(mouse_pos):
                    print(f"Game {i + 1} selected in {self.mode.capitalize()} mode.")
                    # Move to the selected game (this would typically involve changing states or scenes)

    def update(self):
        pass

    def go_back(self):
        print("Going back to the home page...")
        # Here you would typically change the state or scene, e.g., self.manager.change_state("HOME")

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