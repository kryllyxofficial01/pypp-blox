import pygame
import utils

def create_widgets(screen: pygame.Surface) -> None:
    canvas = pygame.Surface(utils.WINDOW_DIMENSIONS)

    blocks_panel = pygame.Rect(
        0, 0,
        utils.WINDOW_DIMENSIONS[0] // 5,
        utils.WINDOW_DIMENSIONS[1]
    )

    preview_window_dimensions = (utils.WINDOW_DIMENSIONS[0] // 4, utils.WINDOW_DIMENSIONS[0] // 6)
    preview_window = pygame.Rect(
        0, 0,
        preview_window_dimensions[0],
        utils.WINDOW_DIMENSIONS[1]
    )

    screen.blit(canvas, (0, 0), blocks_panel)
    screen.blit(
        canvas, (
            utils.WINDOW_DIMENSIONS[0] - preview_window_dimensions[0],
            -(utils.WINDOW_DIMENSIONS[1] - preview_window_dimensions[1])
        ),
        preview_window
    )