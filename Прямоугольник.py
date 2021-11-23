import pygame

if __name__ == '__main__':

    def draw_rect(screen, size):
        pygame.draw.rect(screen, pygame.Color('red'),
                         (1, 1, size[0] - 2, size[1] - 2), 0)


    try:
        pygame.init()
        size = width, height = int(input()), int(input())
        screen = pygame.display.set_mode(size)
        draw_rect(screen, size)
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()
        pygame.quit()
    except Exception as Error:
        print('Неправильный формат ввода')
