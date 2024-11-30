import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
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
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # rotate left
            self.rotate(-dt)

        if keys[pygame.K_d]:
            # rotate right
            self.rotate(dt)

        if keys[pygame.K_w]:
            # move forward
            self.move(-dt)
        
        if keys[pygame.K_s]:
            # move back
            self.move(dt)

    def draw(self, screen):
        # Draw the player as a triangle
        pygame.draw.polygon(screen, "white", self.triangle(), 2)