import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("02-drawing")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with magenta
    screen.fill((255, 0, 255))  

    # Draw a cyan rectangle
    pygame.draw.rect(screen, (0, 255, 255), (50, 50, 200, 100))  

    # Show our drawing on the screen
    pygame.display.flip()