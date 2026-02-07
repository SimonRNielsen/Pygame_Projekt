import pygame

class GameWorld:

    def __init__(self) -> None:
        pygame.init()

        self._screen = pygame.display.set_mode((800,600))
        self._running = True
        self._clock = pygame.time.Clock()

    def awake(self):
        pass

    def start(self):
        pass

    def update(self):
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
            self._screen.fill("cornflowerblue")
            pygame.display.flip()
            self._clock.tick(60)
        pygame.quit()

gw = GameWorld()

gw.awake()
gw.start()
gw.update()