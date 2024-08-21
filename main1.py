import pygame
from loading_page import LoadingPage
from home_page import HomePage


class Game:
    def __init__(self):
        pygame.init()
        screen_info = pygame.display.Info()
        self.width, self.height = int(screen_info.current_w * 0.6), int(screen_info.current_h * 0.8)
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pict-o-word")

        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load("t.png")
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

        self.loading_page = LoadingPage(self.screen)
        self.home_page = HomePage(self.screen, self.bg)
        self.current_page = "loading"

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_event(event)

            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def handle_event(self, event):
        if self.current_page == "loading":
            self.loading_page.handle_event(event)
        elif self.current_page == "home":
            self.home_page.handle_event(event)

    def update(self):
        if self.current_page == "loading":
            self.loading_page.update()
            if self.loading_page.loading_completed:
                self.current_page = "home"
        elif self.current_page == "home":
            self.home_page.update()

    def draw(self):
        if self.current_page == "loading":
            self.loading_page.draw()
        elif self.current_page == "home":
            self.home_page.draw()


if __name__ == "__main__":
    game = Game()
    game.run()