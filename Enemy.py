import pygame, random
from Components import Component
from Enums import Collisions, Components,Collidable

class Enemy(Component):

    def awake(self, game_world):
        sr = self._gameObject.get_component(Components.SPRITERENDERER.value)
        random_x = random.randint(0, game_world.screen.get_width()-sr.sprite_image.get_width())
        self._gameObject.transform.position = pygame.math.Vector2(random_x,0)
        self._screen_size = pygame.math.Vector2(game_world._screen.get_width(),game_world._screen.get_height())
        collider = self._gameObject.get_component(Components.COLLIDER.value)
        collider.subscribe(Collisions.ENTER, self.on_collision_enter)
        collider.subscribe(Collisions.EXIT, self.on_collision_exit)
        collider.subscribe(Collisions.PIXEL_ENTER, self.on_pixel_collision_enter)
        collider.subscribe(Collisions.PIXEL_EXIT, self.on_pixel_collision_exit)
        self._gameObject._subtype = Collidable.ENEMY

    def start(self):
        pass

    def update(self, delta_time):
        speed = 0
        movement = pygame.math.Vector2(0,speed)

        self._gameObject.transform.translate(movement*delta_time)
        bottom_limit = self._screen_size.y

        if self._gameObject.transform.position.y > bottom_limit:
            self._gameObject.destroy()

    def on_collision_enter(self, other):
        print(f"{__class__.__name__}: Collision enter")

    def on_collision_exit(self, other):
        print(f"{__class__.__name__}: Collision exit")

    def on_pixel_collision_enter(self, other):
        print(f"{__class__.__name__}: Pixel collision enter")

    def on_pixel_collision_exit(self, other):
        print(f"{__class__.__name__}: Pixel collision exit")