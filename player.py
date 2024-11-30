import pygame
from constants import PLAYER_RADIUS
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class's constructor
        super().__init__(x, y, PLAYER_RADIUS)
        # Initialize rotation
        self.rotation = 0

    def triangle(self):
        # Create a forward and right vector
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(1, 0).rotate(self.rotation) * self.radius / 1.5
        # Calculate the triangle points
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # Draw the player as a triangle
        pygame.draw.polygon(screen, "white", self.triangle(), 2)