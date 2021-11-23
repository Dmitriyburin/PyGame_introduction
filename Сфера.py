import pygame

if __name__ == '__main__':
    try:
        n = int(input())
    except Exception:
        print('Неправильный формат ввода')
    else:
        pygame.init()
        size = width, height = 300, 300
        screen = pygame.display.set_mode(size)
        h, c = 0, 135
        for j in range(n):
            pygame.draw.ellipse(screen, 'white', (0, abs(c), 300, h + 30), 1)
            h, c = h + 30, c - 15
        h, c = 0, 135
        for j in range(n):
            pygame.draw.ellipse(screen, 'white', (abs(c), 0, h + 30, 300), 1)
            h, c = h + 30, c - 15
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()
        pygame.quit()
