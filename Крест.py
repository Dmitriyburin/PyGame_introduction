import pygame

if __name__ == '__main__':

    def draw_line(screen, size):
        pygame.draw.line(screen, pygame.Color('white'),
                         (0, 0), size, width=5)
        pygame.draw.line(screen, pygame.Color('white'),
                         (size[0], 0), (0, size[0]), width=5)

    try:
        pygame.init()
        pygame.display.set_caption('Крест')
        size = width, height = int(input()), int(input())
        screen = pygame.display.set_mode(size)
        draw_line(screen, size)
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()
        pygame.quit()
    except Exception:
        print('Неправильный формат ввода')
