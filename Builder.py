from abc import ABC, abstractmethod
from GameObject import GameObject
from Components import SpriteRenderer, Animator, Collider
from Player import Player
from Enemy import Enemy
import random, pygame

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
        self._gameObject.add_component(Collider())

    def get_gameObject(self) -> GameObject:
        return self._gameObject
    
class EnemyBuilder(Builder):

    def build(self):
        self._gameObject = GameObject(pygame.math.Vector2(0,0))
        sprites = ["enemy_01.png", "enemy_02.png", "enemy_03.png"]
        selected_sprite = random.choice(sprites)
        self._gameObject.add_component(SpriteRenderer(selected_sprite))
        self._gameObject.add_component(Enemy())
        self._gameObject.add_component(Collider())

    def get_gameObject(self):
        return self._gameObject