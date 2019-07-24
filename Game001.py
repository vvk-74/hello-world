import pygame
pygame.init()
# запуск окна
win = pygame.display.set_mode((500,500))
# Название окна
pygame.display.set_caption('Первая игра')

x = 50
y = 425
width = 40 # ширина
height = 60 # высота
speed = 5

isJump = False
jumpCount = 10
# основной игровой цикл
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
# отслеживание нажатие кнопок
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

# обновление окна
    win.fill((0,0,0))

# создаем игрока
    pygame.draw.rect(win, (0,0,255),(x, y, width, height))
    pygame.display.update()
pygame.quit()

