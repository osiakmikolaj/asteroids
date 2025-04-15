import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()

        dt = clock.tick(60) / 1000

# following ensures that the main() function is only called when 
# this file is run directly; it won't run if it's imported as a module. 
if __name__ == "__main__":
    main()