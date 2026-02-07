import pygame

class GameWorld:

    def __init__(self) -> None:
        pygame.init()

        self._screen = pygame.display.set_mode((1280,1024))
        self._running = True
        self._clock = pygame.time.Clock()

        self._sprite_image = pygame.image.load("assets\\player.png")
        self._sprite = pygame.sprite.Sprite()
        self._sprite.rect = self._sprite_image.get_rect()

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

            self._screen.blit(self._sprite_image,self._sprite.rect)

            pygame.display.flip()
            self._clock.tick(60)
        pygame.quit()

gw = GameWorld()

gw.awake()
gw.start()
gw.update()