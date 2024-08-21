import pygame
import math

class HomePage:
    def __init__(self, screen, background_image):
        self.screen = screen
        self.bg = background_image
        self.width, self.height = screen.get_size()
        self.setup_colors()
        self.setup_fonts()
        self.current_mode = "EASY"
        self.settings_open = False
        self.load_icons()

        # Load the logo
        self.logo = pygame.image.load("Logo transparent4.png")
        self.logo_rect = self.logo.get_rect()
        self.logo_rect.centerx = self.width // 2
        self.logo_rect.y = 50

        # Create shadow for the logo
        self.logo_shadow = self.logo.copy()
        self.logo_shadow.fill((0, 0, 0, 50), special_flags=pygame.BLEND_RGBA_MULT)
        self.logo_shadow_rect = self.logo_shadow.get_rect()
        self.logo_shadow_rect.x = self.logo_rect.x + 9
        self.logo_shadow_rect.y = self.logo_rect.y + 9

    def setup_colors(self):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 127.5 * 0.75, 0)
        self.YELLOW = (255 * 0.65, 255 * 0.65, 0)
        self.RED = (127.5 * 0.75, 0, 0)
        self.PINK = (127.5 * 0.9, 52.5 * 0.9, 90 * 0.9)
        self.LIGHT_BLUE = (86.5 * 0.75, 108 * 0.75, 115 * 0.75)
        self.PALEYELLOW = (225 * 0.75, 225 * 0.75, 100 * 0.75)
        self.YELLOW1 = (255, 255, 0)
        self.PINK1 = (225 * 0.85, 105 * 0.85, 180 * 0.85)


    def setup_fonts(self):
        self.title_font = pygame.font.Font(None, 48)
        self.button_font = pygame.font.Font(None, 36)

    def load_icons(self):
        self.icons = {
            "Music": self.create_music_icon(),
            "Volume": self.create_volume_icon(),
            "Reminder": self.create_reminder_icon(),
            "Need Help?": self.create_help_icon()
        }

    def create_music_icon(self):
        surface = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(surface, self.BLACK, (15, 15), 10, 2)
        pygame.draw.line(surface, self.BLACK, (25, 15), (25, 5), 2)
        return surface

    def create_volume_icon(self):
        surface = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.polygon(surface, self.BLACK, [(5, 15), (15, 5), (15, 25)])
        pygame.draw.arc(surface, self.BLACK, (15, 5, 10, 20), -math.pi/3, math.pi/3, 2)
        return surface

    def create_reminder_icon(self):
        surface = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(surface, self.BLACK, (15, 15), 12, 2)
        pygame.draw.line(surface, self.BLACK, (15, 7), (15, 15), 2)
        pygame.draw.line(surface, self.BLACK, (15, 15), (20, 20), 2)
        return surface

    def create_help_icon(self):
        surface = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(surface, self.BLACK, (15, 15), 13, 2)
        font = pygame.font.Font(None, 24)
        text = font.render("?", True, self.BLACK)
        surface.blit(text, (11, 8))
        return surface

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.draw_logo()
        self.draw_mode_button()
        self.draw_play_button()
        self.draw_exit_button()
        self.draw_settings_icon()
        self.draw_coin_counter()

        if self.settings_open:
            self.draw_settings()

    def draw_logo(self):
        logo_rect = self.logo.get_rect(center=(self.width // 2, 50))
        self.screen.blit(self.logo, logo_rect)

    def draw_mode_button(self):
        colors = {"EASY": self.GREEN, "MEDIUM": self.YELLOW, "HARD": self.RED}
        # Adjusted y-coordinate to move the button down
        y_pos = 330
        self.draw_circle_with_shadow(self.screen, colors[self.current_mode], (self.width // 2, y_pos), 50)
        mode_text = self.button_font.render(self.current_mode, True, self.WHITE)
        mode_rect = mode_text.get_rect(center=(self.width // 2, y_pos))
        self.screen.blit(mode_text, mode_rect)

        if self.current_mode != "EASY":
            pygame.draw.polygon(self.screen, self.WHITE,
                                [(self.width // 2 - 80, y_pos), (self.width // 2 - 60, y_pos - 10), (self.width // 2 - 60, y_pos + 10)])
        if self.current_mode != "HARD":
            pygame.draw.polygon(self.screen, self.WHITE,
                                [(self.width // 2 + 80, y_pos), (self.width // 2 + 60, y_pos - 10), (self.width // 2 + 60, y_pos + 10)])

    def draw_play_button(self):
        # Adjusted y-coordinate to move the button further down
        y_pos = 430
        # Increase the size of the rectangle
        self.draw_rect_with_shadow(self.screen, self.PALEYELLOW, (self.width // 2 - 90, y_pos, 180, 60), border_radius=15)
        play_text = self.button_font.render("PLAY", True, self.WHITE)
        play_rect = play_text.get_rect(center=(self.width // 2, y_pos + 30))
        self.screen.blit(play_text, play_rect)

    def draw_exit_button(self):
        # Adjusted y-coordinate to move the button further down
        y_pos = 530
        # Increase the size of the rectangle
        self.draw_rect_with_shadow(self.screen, self.PINK1, (self.width // 2 - 90, y_pos, 180, 60), border_radius=15)
        exit_text = self.button_font.render("EXIT", True, self.WHITE)
        exit_rect = exit_text.get_rect(center=(self.width // 2, y_pos + 30))
        self.screen.blit(exit_text, exit_rect)

    def draw_settings_icon(self):
        self.draw_circle_with_shadow(self.screen, self.PINK1, (40, 40), 20)
        for i in range(3):
            y = 33 + i * 7
            pygame.draw.line(self.screen, self.WHITE, (30, y), (50, y), 2)

    def draw_coin_counter(self):
        self.draw_rect_with_shadow(self.screen, self.PINK1, (self.width - 130, 20, 110, 40), border_radius=20)
        pygame.draw.circle(self.screen, self.YELLOW1, (self.width - 110, 40), 15)
        pygame.draw.circle(self.screen, self.BLACK, (self.width - 110, 40), 15, 2)
        coin_text = self.button_font.render("50", True, self.WHITE)
        coin_rect = coin_text.get_rect(center=(self.width - 60, 40))
        self.screen.blit(coin_text, coin_rect)

    def draw_settings(self):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        self.screen.blit(overlay, (0, 0))

        settings_surface = pygame.Surface((300, 400), pygame.SRCALPHA)
        settings_surface.fill((173, 216, 230, 200))  # Light blue with some transparency

        settings_title = self.title_font.render("SETTINGS", True, self.BLACK)
        settings_surface.blit(settings_title, (75, 20))

        options = ["Music", "Volume", "Reminder", "Need Help?"]
        for i, option in enumerate(options):
            text = self.button_font.render(option, True, self.BLACK)
            settings_surface.blit(text, (70, 100 + i * 60))
            settings_surface.blit(self.icons[option], (30, 95 + i * 60))

        self.screen.blit(settings_surface, (self.width // 2 - 150, self.height // 2 - 200))

    def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if self.settings_open:
                    if not self.is_point_inside(mouse_pos, (self.width // 2 - 150, self.height // 2 - 200, 300, 400)):
                        self.settings_open = False
                else:
                    y_pos = 330  # Adjust to match the new y-position for the mode button

                    # Check for right arrow (next mode)
                    if self.is_point_inside(mouse_pos, (self.width // 2 + 60, y_pos - 10, 20, 20)):
                        self.cycle_mode(1)
                    # Check for left arrow (previous mode)
                    elif self.is_point_inside(mouse_pos, (self.width // 2 - 80, y_pos - 10, 20, 20)):
                        self.cycle_mode(-1)
                    # Check for settings icon
                    elif self.is_point_inside(mouse_pos, (20, 20, 40, 40)):
                        self.settings_open = True
                    # Check for play button
                    elif self.is_point_inside(mouse_pos, (self.width // 2 - 90, 450, 180, 60)):
                        print("Play button clicked")  # Replace with actual play logic
                    # Check for exit button
                    elif self.is_point_inside(mouse_pos, (self.width // 2 - 90, 530, 180, 60)):
                        pygame.quit()
                        quit()



    def is_point_inside(self, point, rect):
        x, y = point
        rx, ry, rw, rh = rect
        return rx <= x <= rx + rw and ry <= y <= ry + rh

    def cycle_mode(self, direction):
        modes = ["EASY", "MEDIUM", "HARD"]
        current_index = modes.index(self.current_mode)
        new_index = (current_index + direction) % 3
        self.current_mode = modes[new_index]

    def draw_circle_with_shadow(self, surface, color, center, radius):
        shadow = pygame.Surface((radius * 2 + 4, radius * 2 + 4), pygame.SRCALPHA)
        pygame.draw.circle(shadow, (0, 0, 0, 64), (radius + 2, radius + 2), radius)
        surface.blit(shadow, (center[0] - radius - 2, center[1] - radius - 2))
        pygame.draw.circle(surface, color, center, radius)

    def draw_rect_with_shadow(self, surface, color, rect, border_radius=0):
        shadow = pygame.Surface((rect[2] + 4, rect[3] + 4), pygame.SRCALPHA)
        pygame.draw.rect(shadow, (0, 0, 0, 64), (2, 2, rect[2], rect[3]), border_radius=border_radius)
        surface.blit(shadow, (rect[0] - 2, rect[1] - 2))
        pygame.draw.rect(surface, color, rect, border_radius=border_radius)

    def draw_logo(self):
        # Draw the logo shadow
        self.screen.blit(self.logo_shadow, self.logo_shadow_rect)
        # Draw the logo
        self.screen.blit(self.logo, self.logo_rect)

    def update(self):
        pass  # Add any update logic here if needed