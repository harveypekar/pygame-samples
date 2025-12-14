import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Input Keyboard")

running = True


fill_color = (0, 0, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                fill_color = (255, 255, 255)
        elif event.type == pygame.KEYUP:
            fill_color = (0, 0, 0)
    
    screen.fill(fill_color)  

    pygame.display.flip()