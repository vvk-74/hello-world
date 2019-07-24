import pygame
pygame.init()

display_width = 800
display_heidht = 600

display = pygame.display.set_mode((display_width, display_heidht))
pygame.display.set_caption('Дино')

def run_game():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill((255, 255, 255))

run_game()

