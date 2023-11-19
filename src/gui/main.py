import pygame

FPS = 30
EDITOR_BG_COLOR = (174, 198, 207)

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((600, 800))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(EDITOR_BG_COLOR)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()