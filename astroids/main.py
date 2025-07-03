import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main(): 
    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))     
    clock = pygame.time.Clock()  # Set the frame rate to 60 FPS
  
    updatable = pygame.sprite.Group()  # Create a group for updatable objects
    drawable = pygame.sprite.Group()  # Create a group for drawable objects
    asteroids = pygame.sprite.Group()  # Create a group for asteroids
    shots = pygame.sprite.Group()  # Create a group for shots

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)  # Add shots to the updatable and drawable groups
    AsteroidField.containers = updatable  # Add the asteroid field to the updatable group
    asteroid_field = AsteroidField()  # Create the asteroid field
    
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Create the player at the center of the screen

    dt = 0

    # Main game loop    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        updatable.update(dt)
        
        for asteroid in asteroids:             
            if asteroid.collides_with(player):            
                print("Game Over!")
                sys.exit()
                    
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")  # Fill the screen with black

        for obj in drawable:  # Update and draw all drawable objects 
            obj.draw(screen)  # Draw the object on the screen

        pygame.display.flip()  # Update the display

        dt = clock.tick(60) / 1000.0
        
print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")
    

if __name__ == "__main__":
    main()