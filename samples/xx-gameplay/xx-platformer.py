import pygame

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Input Keyboard")

running = True

## this is how fast we're jumping up (when positive), or falling down (when negative)
speed_y = 0

player_position = [20, 50]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                # check if we're on the ground. If we don't do this, you can jump in the air

                # set our vertical speed up
                speed_y = -10
        elif event.type == pygame.KEYUP:
            fill_color = (0, 0, 0)
    
    screen.fill((0, 0, 0))  


    # Draw a cyan rectangle
    pygame.draw.rect(screen, (0, 255, 255), (50, 50, 200, 100))  

    pygame.display.flip()