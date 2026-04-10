import pygame

pygame.init()

debug_mode = True

screen = pygame.display.set_mode((600,336))

mario = pygame.image.load('mariomove.gif')
mario = pygame.transform.scale(mario, (mario.get_width()*.2, mario.get_height()*.2))

backg = pygame.image.load('background.png')
backg = pygame.transform.scale(backg, (backg.get_width()*2, backg.get_height()*2))

#floor_rect = pygame.Rect(0,300,600,36) #x,y,width, height

#NEW Changing our floor to platforms THEY ALL HAVE THE SAME BEHAVIOR
platforms = [
    pygame.Rect(0, 300, 600, 36),   # floor
    pygame.Rect(200, 220, 120, 20), # floating platform
    pygame.Rect(400, 160, 100, 20)  # another one
]

#NEW adding physics variables
vy = 0
gravity = 0.3
on_ground = False

clock = pygame.time.Clock()

running = True
x = 0
y = 220
while running:
    #Single key presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #OLD CODE WE COMMENTED OUT
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_SPACE and on_ground:
                #vy = -8 #Set speed rather than moving character up

    #Continuous movement press/press and hold
    keys = pygame.key.get_pressed()
    #NEW Move space into keys pressed
    if keys[pygame.K_SPACE] and on_ground:
        vy = -8 #Set speed rather than moving character up
        on_ground = False
    if keys[pygame.K_UP]:
        y = y-1
    if keys[pygame.K_DOWN]:
        y = y+1
    if keys[pygame.K_LEFT]:
        x = x-1
    if keys[pygame.K_RIGHT]:
        x = x+1


    #NEW apply gravity every frame
    vy = gravity + vy
    y = vy + y

    mario_rect = mario.get_rect(topleft=(x,y))

    #NEW
    #First set ground to false, don't assume player is on ground
    on_ground = False

    #Loop through every platform to check for a collision
    for platform in platforms:
        if mario_rect.colliderect(platform): #If there is a collision
            # Only land if already falling
            if vy > 0 and mario_rect.bottom <= platform.bottom: #If we have speed, and if mario is below the platform
                y = platform.top - mario_rect.height #Placing mario on top
                vy = 0 #Set speed to 0
                on_ground = True #enable jump by saying he's on a platform

    #NEW Move draws until after the collisions
    screen.blit(backg, (0,0))
    screen.blit(mario, (x, y))
    if debug_mode == True:
        pygame.draw.rect(screen, (0, 255, 0), mario_rect, 2)
        #NEW DRAW OUR PLATFORMS IN WHITE
        for platform in platforms:
            pygame.draw.rect(screen, (255, 255, 255), platform, 2)

    clock.tick(60)

    pygame.display.flip()

pygame.quit()
