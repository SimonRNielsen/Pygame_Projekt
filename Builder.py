from abc import ABC, abstractmethod
from GameObject import GameObject
from Components import SpriteRenderer, Animator
from Player import Player
import pygame

class Builder(ABC):

    @classmethod
    @abstractmethod
    def build(self):
        pass

    def get_gameObject(self) -> GameObject:
        pass

class PlayerBuilder(Builder):

    def build(self):
        self._gameObject = GameObject(pygame.math.Vector2(0,0))
        self._gameObject.add_component(SpriteRenderer("player.png"))
        self._gameObject.add_component(Player())
        animator = self._gameObject.add_component(Animator())
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

    def get_gameObject(self) -> GameObject:
        return self._gameObject