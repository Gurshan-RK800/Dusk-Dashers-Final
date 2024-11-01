import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 700))
player = pygame.Rect(600, 350, 50, 50)
movement_speed = 2

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= movement_speed
    if keys[pygame.K_s]:
        player.y += movement_speed
    if keys[pygame.K_a]:
        player.x -= movement_speed
    if keys[pygame.K_d]:
        player.x += movement_speed

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), player)
    pygame.display.update()

pygame.quit()
