import pygame

pygame.init()

surface = pygame.display.set_mode((800,800))
color = (255,0,0)

clock = pygame.time.Clock()
FPS = 60  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BOARD_COLOR = BLUE
SCREEN_COLOR = WHITE
# pygame.draw.rect(surface, color, pygame.Rect(100,150,200, 150))
rect = pygame.Rect((0, 0), (32, 32))
image = pygame.Surface((32, 32))
image .fill(RED) 

board = pygame.Surface((400,800))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                rect.move_ip(0, -2)
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                rect.move_ip(0, 2)
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                rect.move_ip(-2, 0)
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                rect.move_ip(2, 0)
    surface.fill(SCREEN_COLOR)
    surface.blit(image, rect)
    surface.blit(board, (0,0))
    pygame.display.flip()

