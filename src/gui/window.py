import pygame
import utils

def create_widgets(screen: pygame.Surface) -> None:
    canvas = pygame.Surface(utils.WINDOW_DIMENSIONS)

    width = utils.WINDOW_DIMENSIONS[0]
    height = utils.WINDOW_DIMENSIONS[1]

    blocks_panel = pygame.Rect(
        0, 0, width // 5, height
    )

    preview_window_dimensions = (
        width // 4, width // 6
    )
    preview_window = pygame.Rect(
        0, 0, preview_window_dimensions[0], height
    )

    screen.blit(canvas, (0, 0), blocks_panel)
    screen.blit(
        canvas, (
            width - preview_window_dimensions[0],
            -(height - preview_window_dimensions[1])
        ),
        preview_window
    )