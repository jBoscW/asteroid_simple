import pygame, sys
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shots, updatables, drawables)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidz_object = AsteroidField()

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000

        pygame.Surface.fill(screen, 'brown')

        for i in drawables:
            i.draw(screen)
        updatables.update(dt)

        for a in asteroids: 
            if a.collides_with(player1):
                print("Game Over!")
                sys.exit()
            
            for b in shots: 
                if a.collides_with(b): 
                    a.split()
                    b.kill()

        pygame.display.flip()

        
        
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
