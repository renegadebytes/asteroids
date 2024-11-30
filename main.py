# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    # initialize pygame
    pygame.init()

    # set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    BLACK = (0, 0, 0)

    # Create the player in the middle of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print(f"")

    # Creating groups for updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Adding player to both groups
    updatable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Clear the screen
        screen.fill(BLACK)

        # Update all updatable objects
        dt = clock.tick(60) / 1000
        for obj in updatable:
            obj.update(dt)

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()