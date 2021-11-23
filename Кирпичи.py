import pygame

if __name__ == '__main__':

    try:
        w, h = 30, 15
    except Exception:
        print('Неправильный формат ввода')
    else:
        pygame.init()
        size = width, height = 300, 200
        screen = pygame.display.set_mode(size)
        screen.fill(pygame.Color('white'))
        count = 0
        for j in range(0, size[0], h + 2):
            count += 1
            margin = -15 if count % 2 == 0 else 0
            for i in range(margin, size[0], w + 2):
                pygame.draw.rect(screen, 'red', (i, j, w, h), 0)
                print(i, j)

        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()
        pygame.quit()
