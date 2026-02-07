import pygame
from GameObject import GameObject
from Components import SpriteRenderer, Animator

class GameWorld:

    def __init__(self) -> None:
        pygame.init()
        self._gameObjects = []

        go = GameObject(pygame.math.Vector2(0,0))
        go.add_component(SpriteRenderer("player.png"))
        animator = go.add_component(Animator())
        animator.add_animation("Idle", 
                               "player02.png", 
                               "player03.png", 
                               "player04.png", 
                               "player05.png", 
                               "player06.png", 
                               "player07.png", 
                               "player08.png", 
                               "player07.png", 
                               "player06.png", 
                               "player05.png", 
                               "player04.png", 
                               "player03.png",)
        animator.play_animation("Idle")
        self._gameObjects.append(go)

        self._screen = pygame.display.set_mode((1280,720))
        self._running = True
        self._clock = pygame.time.Clock()

    @property
    def screen(self):
        return self._screen

    def awake(self):
        for gameObject in self._gameObjects[:]:
            gameObject.awake(self)

    def start(self):
        for gameObject in self._gameObjects[:]:
            gameObject.start()

    def update(self):
        while self._running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

            self._screen.fill("cornflowerblue")
            delta_time = self._clock.tick(60) / 1000.0

            for gameObject in self._gameObjects[:]:
                gameObject.update(delta_time)

            pygame.display.flip()

        pygame.quit()

gw = GameWorld()

gw.awake()
gw.start()
gw.update()