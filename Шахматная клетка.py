import pygame

if __name__ == '__main__':

    def draw_rect(screen, cur, color):
        pygame.draw.rect(screen, color, cur, 0)


    try:
        pygame.init()
        user = input().split()
        size = (int(user[0]), int(user[0]))
        n = size[0] // int(user[1])
    except Exception:
        print('Неправильный формат ввода')
    else:
        screen = pygame.display.set_mode(size)
        screen.fill(pygame.Color('#ffffff'))
        count2 = 0
        for j in range(size[0], 0 - n, -n):
            count2 += 1
            count = 0
            for i in range(0, size[0], n):
                count += 1
                color = 'white' if (count + count2) % 2 == 0 else 'black'
                print(i, j, count, color)
                draw_rect(screen, (i, j, n, n), color)
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()
        pygame.quit()
