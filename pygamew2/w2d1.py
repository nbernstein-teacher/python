import pygame

pygame.init()

screen = pygame.display.set_mode((600,336))

mario = pygame.image.load('mariomove.gif')
mario = pygame.transform.scale(mario, (mario.get_width()*.2, mario.get_height()*.2))

backg = pygame.image.load('background.png')
backg = pygame.transform.scale(backg, (backg.get_width()*2, backg.get_height()*2))

#Creating a rectangle for the floor
floor_rect = pygame.Rect(0, 300, 600, 36) #x,y,width,height
floor_color = (255, 255, 255)

#Choosing whether debug mode is on or off
debug_mode = True

clock = pygame.time.Clock()

running = True
x = 0
y = 240
while running:
    screen.fill((0,0,0))
    screen.blit(backg, (0,0))
    screen.blit(mario, (x, y))

    #create a new mario_rect to give mario a hitbox
    mario_rect = mario.get_rect(topleft=(x,y))
    #Actually draw mario's hitbox - only if debug mode is on!
    if debug_mode == True:
        pygame.draw.rect(screen, (0, 255, 0), mario_rect, 2)

    #Single key presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y = y-10

    #Continuous movement press/press and hold
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y = y-1
    if keys[pygame.K_DOWN]:
        y = y+1
        #add collision detection
        if mario_rect.colliderect(floor_rect):
            y = y-1
            floor_color = (255, 0, 0)
    if keys[pygame.K_LEFT]:
        x = x-1
    if keys[pygame.K_RIGHT]:
        x = x+1

    clock.tick(60)

    #Draw the floor box, only if debug is true!
    if debug_mode == True:
        pygame.draw.rect(screen, floor_color, floor_rect)

    pygame.display.flip()

pygame.quit()
