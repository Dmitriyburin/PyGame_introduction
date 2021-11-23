import pygame

if __name__ == '__main__':

    def draw_rect(screen, cur, color):
        pygame.draw.rect(screen, color, cur, 0)


    try:
        pygame.init()
        user = input().split()
        w, n = int(user[0]), int(user[1])
    except Exception:
        print('Неправильный формат ввода')
    else:
        size = width, height = 300, 300
        screen = pygame.display.set_mode(size)
        screen.fill(pygame.Color(0, 0, 0))
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        for i in range(n):
            color = colors[i % 3]
            pygame.draw.circle(screen, color, (width // 2, height // 2), width // 2 - w * i)
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()
        pygame.quit()
