from abc import ABC, abstractmethod
import pygame

class Component(ABC):

    def __init__(self) -> None:
        super().__init__()
        self._gameObject = None

    @property
    def gameObject(self):
        return self._gameObject
    
    @gameObject.setter
    def gameObject(self,value):
        self._gameObject = value

    @abstractmethod
    def awake(self, game_world):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self, delta_time):
        pass

class SpriteRenderer(Component):

    def __init__(self, sprite_name) -> None:
        super().__init__()

        self._sprite_image = pygame.image.load(f"assets\\{sprite_name}")
        self._sprite = pygame.sprite.Sprite()
        self._sprite.rect = self._sprite_image.get_rect()

    def awake(self, game_world):
        self._game_world = game_world

    def start(self):
        pass

    def update(self, delta_time):
        self._game_world.screen.blit(self._sprite_image,self._sprite.rect)