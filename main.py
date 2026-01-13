import pygame
from logger import log_state
from player import Player

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH


def main():

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(x,y)
    dt = 0



    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
       

        #Limit timeframe to 60 fps
        dt = clock.tick(60) /1000


if __name__ == "__main__":
    main()
