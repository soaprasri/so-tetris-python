import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BOARD_COLOR = BLUE
SCREEN_COLOR = WHITE

screen = pygame.display.set_mode((800,800))
screen.fill(SCREEN_COLOR)
image = pygame.image.load(r'/Users/soaprateek/Downloads/20440546.bmp')
done = False
i = 10
while not done:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            done = True
    screen.fill(SCREEN_COLOR)
    screen.blit(image,(0,0))
    pygame.draw.rect(screen, (GREEN), pygame.Rect(30+i,30+i,30,30))
    pygame.draw.rect(screen, (RED), pygame.Rect(0,0,30,30))
    i = i+ 1
    pygame.display.flip()
