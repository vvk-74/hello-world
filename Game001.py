import pygame
pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Дино')

icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

def run_game():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill((255, 255, 255))
        pygame.display.update()

run_game()

