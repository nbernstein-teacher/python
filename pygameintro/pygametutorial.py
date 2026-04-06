import pygame

pygame.init()

screen = pygame.display.set_mode((600,336))

baseball = pygame.image.load('mariomove.gif')
baseball = pygame.transform.scale(baseball, (baseball.get_width()*.2, baseball.get_height()*.2))

backg = pygame.image.load('background.png')
backg = pygame.transform.scale(backg, (backg.get_width()*2, backg.get_height()*2))

clock = pygame.time.Clock()

running = True
x = 0
y = 240
while running:
    screen.fill((0,0,0))
    screen.blit(backg, (0,0))
    screen.blit(baseball, (x, y))
    #x += .5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y = y-5
        '''
            if event.key == pygame.K_UP:
                y = y-1
            if event.key == pygame.K_DOWN:
                y += 5
            if event.key == pygame.K_LEFT:
                x -= 5
            if event.key == pygame.K_RIGHT:
                x += 5
        '''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y = y-1
    if keys[pygame.K_DOWN]:
        y = y+1
    if keys[pygame.K_LEFT]:
        x = x-1
    if keys[pygame.K_RIGHT]:
        x = x+1

    clock.tick(60)

    pygame.display.flip()

pygame.quit()
