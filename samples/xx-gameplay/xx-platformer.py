import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Input Keyboard")

running = True

clock = pygame.time.Clock()

# this is how fast we're jumping up (when positive), or falling down (when negative)
speed_y = 0

jump_speed = -2.0

# this is how fast we're moving left/right. It's static
speed_x_input = 1.0
speed_x = 0

player_position = [20, 50]
player_dimensions = [50, 50]

world_boxes = (
    ((-10000, 550, 20000, 50),  (0, 255, 0)), #ground
    #((100, 400, 200, 50),  (255, 0, 0)) #platform
)

left_down = False
right_down = False
space_down = False

while running:

    elapsed_time = clock.tick()

    # first, we want to apply gravity. We don't care if we're on th ground, 
    # as we'll account for that later. This is an unusual way to do it, but it's simple.

    gravity = 0.5 # how much we change the speed per second

    speed_y += gravity * elapsed_time
    increase = speed_y * elapsed_time
    player_position[1] += increase

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                # set our vertical speed up
                space_down = True
            elif event.key == pygame.K_LEFT:
                left_down = True   
            elif event.key == pygame.K_RIGHT:
                right_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space_down = False
            elif event.key == pygame.K_LEFT:
                left_down = False   
            elif event.key == pygame.K_RIGHT:
                right_down = False
    

    screen.fill((0, 0, 0))  

    touching = False
    for box in world_boxes:
        pygame.draw.rect(screen, box[1], box[0])  
        box_rect = pygame.Rect(box[0])
        player_rect = pygame.Rect(player_position[0], player_position[1],
                                    player_dimensions[0], player_dimensions[1]) 
        
        
        # Draw a cyan rectangle
        pygame.draw.rect(screen, (0, 255, 255), (player_position[0], player_position[1],
                                                player_dimensions[0], player_dimensions[1]))  

        pygame.display.flip()
        
        if player_rect.colliderect(box_rect):
            # we hit something! Move the player up to the top of the box
            player_position[1] = box[0][1] - player_dimensions[1]
            speed_y = 0  # stop falling/jumping
            touching = True

    speed_x = 0
    if left_down:
            speed_x -= speed_x_input * elapsed_time
    if right_down:
        speed_x += speed_x_input * elapsed_time
        
    #if touching:
    if space_down:
        speed_y = jump_speed
        player_position[0] += speed_x * elapsed_time
        player_rect = pygame.Rect(player_position[0], player_position[1],
                                    player_dimensions[0], player_dimensions[1])



    # Draw a cyan rectangle
    pygame.draw.rect(screen, (0, 255, 255), (player_position[0], player_position[1],
                                             player_dimensions[0], player_dimensions[1]))  

    pygame.display.flip()