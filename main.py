import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #
    ### Variables
    #
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    fps = 60
    screen_background = 'black'

    #
    ### Game Loop
    #
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(screen_background)
        pygame.display.flip()
        dt = clock.tick(fps)/1000

if __name__ == "__main__":
    main()
