import pygame
#Initialize pygame
pygame.init()
#Set your screen size to 600, 600 - 1 point
screen = pygame.display.set_mode((600,600))
#Create a green "player" rectangle and put it on the screen - 2 point
x = 0
y = 300

#Use this image as your background (no resizing needed) - https://panolam.com/wp-content/uploads/2022/09/GRID-OVERLAY-01-600x600.jpg - 1 point
backg = pygame.image.load('background.jpg')
#Create 2-3 red "wall" rectangles and put them on the screen - 1 point
walls = [
    pygame.Rect(300, 300, 50, 10),
    pygame.Rect(400, 100, 10, 70),
    pygame.Rect(10, 0, 50, 10)
]
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Move your green player icon around using smooth movement using the arrow keys or ASWD - 4 points
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        y = y+1
    if keys[pygame.K_LEFT]:
        x = x-1
    if keys[pygame.K_UP]:
        y = y-1
    if keys[pygame.K_RIGHT]:
        x = x+1

    player_rect = pygame.Rect(x, y, 30, 30)

    #Create at least one collision check that stops the green block from entering the red block from one direction. - 1 point
    for wall in walls:
        if player_rect.colliderect(wall):
            x = wall.left - player_rect.width

    screen.blit(backg, (0,0))
    for wall in walls:
        pygame.draw.rect(screen, (255,0,0), wall, 2)
    pygame.draw.rect(screen, (0,255,0), player_rect, 2)

    clock.tick(60)
    pygame.display.flip()
pygame.quit()
