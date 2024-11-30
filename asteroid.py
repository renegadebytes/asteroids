import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent class's constructor
        super().__init__(x, y, radius)
        # Initialize rotation

    def draw(self, screen):
        # Draw the player as a triangle
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
  
    def update(self, dt):
        self.position += self.velocity * dt