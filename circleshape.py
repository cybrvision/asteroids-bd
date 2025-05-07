import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def check_collision(self, c2) -> bool:
        col_distance = self.radius + c2.radius
        object_distance = self.position.distance_to(c2.position)
        ###print(f"Collision distance: {col_distance}")
        ###print(f"Distance to Obj: {object_distance}")
        return object_distance <= col_distance
            

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass