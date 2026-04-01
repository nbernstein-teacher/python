import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

baseball = pygame.image.load('baseball.jpg')

clock = pygame.time.Clock()

running = True
x = 0
while running:

    screen.blit(baseball, (x, 0))
    x += .5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)

    pygame.display.flip()

pygame.quit()
