import pygame


# pygame setup
class LoadingPage:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        # Get the current screen size using pygame.display.Info()
        screen_info = pygame.display.Info()
        pygame.display.set_caption("Pict-o-word")

        # Set the window size to 80% of the user's screen size
        self.size = self.width, self.height = int(screen_info.current_w * 0.6), int(screen_info.current_h * 0.8)

        self._running = True
        self._display_surf = None
        self.clock = pygame.time.Clock()
        self.screen = None
        self.bg = pygame.image.load("t.png")
        self.logo = pygame.image.load("Logo3.png")
        self.bg = pygame.transform.scale(self.bg, self.size)

        # Get the rectangle of the image
        self.logo_rect = self.logo.get_rect()
        self.logo_rect.centerx = self.size[0] // 2
        self.logo_rect.y = 50
        self.loading_progress = 0
        self.loading_speed = 2
        self.loading_completed = False
        self.bar_width = 450
        self.bar_height = 50
        self.bar_x = (self.width - self.bar_width) // 2
        self.bar_y = self.height - 200
        self.BLUE = (0, 102, 204)
        self.YELLOW = (255, 255, 100)
        self.WHITE = (255, 255, 255)
        self.font = None
        self.word_of_the_day = "Claustrophobic"
        self.shadow = self.logo.copy()
        self.shadow.fill((0, 0, 0, 50), special_flags=pygame.BLEND_RGBA_MULT)

    def on_init(self):
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.font = pygame.font.Font(None, 36)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.logo, self.logo_rect)

        pygame.draw.rect(self.screen, self.WHITE, (self.bar_x, self.bar_y, self.bar_width, self.bar_height), 2,
                         border_radius=25)

        # self.loading_progress += self.loading_speed
        # if self.loading_progress > self.bar_width:
        #     self.loading_progress = 0

        pygame.draw.rect(self.screen, self.YELLOW, (self.bar_x, self.bar_y, int(self.loading_progress), self.bar_height), 0, border_radius=25)

        if not self.loading_completed:
            self.loading_progress += self.loading_speed
            if self.loading_progress >= self.bar_width:
                self.loading_progress = self.bar_width
                self.loading_completed = True

        loading_text = self.font.render("LOADING...", True, self.WHITE)
        text_x = self.bar_x + (self.bar_width - loading_text.get_width()) // 2
        text_y = self.bar_y + (self.bar_height - loading_text.get_height()) // 2
        shadow_text = self.font.render("LOADING...", True, (0,0,0))

        self.screen.blit(shadow_text, (text_x + 2, text_y + 2))
        self.screen.blit(loading_text, (text_x, text_y))

        word_text = self.font.render(f"Word of the day: {self.word_of_the_day}", True, self.WHITE)
        word_text_x = (self.width - word_text.get_width()) // 2
        word_text_y = self.bar_y + self.bar_height + 80  # Positioned below the loading bar
        self.screen.blit(word_text, (word_text_x, word_text_y))

        shadow_offset = (9, 9)
        self.screen.blit(self.shadow, (self.logo_rect.x + shadow_offset[0], self.logo_rect.y + shadow_offset[1]))

        # flip() the display to put your work on screen
        pygame.display.flip()
        self.clock.tick(60)  # limits FPS to 60

        if self.loading_completed:
            pygame.time.wait(1000)
            self.move_to_next_phase()

    def on_render(self):
        pass

    def move_to_next_phase(self):
        print("Loading completed. Moving to the next phase.")
        # Add your code here to transition to the next part of your game
        self._running = False

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

# class HomePage:
#     def __init__(self):
#         self.


if __name__ == "__main__":
    theApp = LoadingPage()
    theApp.on_execute()
