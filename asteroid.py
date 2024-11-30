import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

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

    def split(self):
        # Kill the current asteroid
        self.kill()

        # Check if the asteroid is too small to split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # No splitting for small asteroids

        # Generate the new radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate a random angle for the split trajectory
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors for the split
        velocity1 = self.velocity.rotate(random_angle) * 1.2  # Slightly faster
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Spawn two new smaller asteroids
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity2
