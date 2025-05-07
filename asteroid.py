from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius=radius)

    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius)


    def update(self, dt):
        self.position += (self.velocity * dt)

    
    def split(self):
        """Splits the asteroids based on size"""
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            # Smallest asteroid
            return
        else:
            # spawn 2 new smaller asteroids
            random_angle = random.uniform(20.0, 50.0)
            v_plus = self.velocity.rotate(random_angle)
            v_minus = self.velocity.rotate(-1*random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = v_plus*1.2
            a2.velocity = v_minus*1.2





