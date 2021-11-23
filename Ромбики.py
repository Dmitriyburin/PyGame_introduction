import pygame

if __name__ == '__main__':

    try:
        n = int(input())
    except Exception:
        print('Неправильный формат ввода')
    else:
        pygame.init()
        size = width, height = 900, 300
        screen = pygame.display.set_mode(size)
        screen.fill(pygame.Color('yellow'))
        for j in range(0, size[0], n):
            for i in range(0, size[0], n):
                print(i, j)
                if i + n <= width and j + n <= height:
                    pygame.draw.polygon(screen, 'orange', ((i + n // 2, j),
                                                           (i, j + n // 2),
                                                           (i + n // 2, j + n),
                                                           (i + n, j + n // 2)))
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()
        pygame.quit()
