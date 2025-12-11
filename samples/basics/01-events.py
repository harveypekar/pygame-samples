import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("01-input-keyboard")

running = True
while running:
    for event in pygame.event.get():    #get all the events 
        if event.type == pygame.QUIT:   #we are only looking for the QUIT event (cross on the window is clicked)
            running = False             #if we get the QUIT event, we set running to False so the loop finishes, and our game finishes