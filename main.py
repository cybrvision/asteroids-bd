import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #
    ### Variables
    #
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    ## Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player_shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (player_shots, updatable, drawable)

    
    dt = 0
    fps = 60
    screen_background = 'black'
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x, y)
    AsteroidField()


    #
    ### Game Loop
    #
    while True:
        # PROCESSING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # RENDERING
        screen.fill(screen_background)
        updatable.update(dt)

        ## check for collisions
        for asteroid in asteroids.sprites():
            if player.check_collision(asteroid):
                print("Game over!")
                exit(1)
            for bullet in player_shots.sprites():
                if asteroid.check_collision(bullet):
                    asteroid.split()
                    bullet.kill()
        
        ## Draw sprites
        for sprite in drawable.sprites():
            sprite.draw(screen)
        pygame.display.flip()

        # LOGIC
        dt = clock.tick(fps)/1000

if __name__ == "__main__":
    main()
