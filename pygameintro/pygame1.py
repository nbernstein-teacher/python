import pygame

pygame.init()

screen = pygame.display.set_mode((640,640))

mario = pygame.image.load('mariomove.gif').convert_alpha()
#New code to change the size of the image
mario = pygame.transform.scale(mario, (mario.get_width()*.2, mario.get_height()*.2))

#Add a background image
backgroundimg = pygame.image.load('background.png')
#Scale background image
backgroundimg = pygame.transform.scale(backgroundimg, (backgroundimg.get_width()*3, backgroundimg.get_height()*3))

clock = pygame.time.Clock()

running = True
x = 0
#add a y
y = 0
while running:
    #NEW CODE - changes background to white
    #Also makes it so we refresh the screen every frame
    #screen.fill((255,255,255))

    #Add a background image
    screen.blit(backgroundimg, (0,0))



    screen.blit(mario, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #NEW CODE FOR KEYMAPS - Individual single presses
        '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                y -= 5
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y += 5
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x -= 5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x += 5
        '''
    #NEW CODE FOR LONG KEY HOLDS
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= 3
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += 3
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= 3
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += 3

    clock.tick(60)

    pygame.display.flip()

pygame.quit()
