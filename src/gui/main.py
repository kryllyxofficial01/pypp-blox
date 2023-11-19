import pygame
import utils, window

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(utils.WINDOW_DIMENSIONS, flags=pygame.SCALED)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(utils.EDITOR_BG_COLOR)

        window.create_widgets(screen)

        pygame.display.flip()

        clock.tick(utils.FPS)

    pygame.quit()