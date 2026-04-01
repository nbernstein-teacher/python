import pygame

pygame.init()

screen = pygame.display.set_mode((640,640))

mario = pygame.image.load('mario.png').convert()

clock = pygame.time.Clock()

running = True
x = 0
while running:
    screen.blit(mario, (x, 30))

    x += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

    pygame.display.flip()

pygame.quit()
