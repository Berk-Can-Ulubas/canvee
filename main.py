import pygame

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

yellow = (255,255,0)
red = (255,0,0) 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Changing screen color
#screen.fill((255, 255, 0))
#pygame.display.flip()

player = pygame.Rect(300, 350, 50, 50)
player_speed = 1

# Main game loop
while True:
    screen.fill(yellow)
    pygame.draw.rect(screen, red, player)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and player.left > 0: 
        player.move_ip(-player_speed, 0)
    if key[pygame.K_d] and player.right < SCREEN_WIDTH:
        player.move_ip(player_speed, 0)
    if key[pygame.K_w] and player.top > 0:  
        player.move_ip(0, -player_speed)
    if key[pygame.K_s] and player.bottom < SCREEN_HEIGHT:
        player.move_ip(0, player_speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()