import pygame
import random

if __name__ == '__main__':

    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('#ffffff'))


    def draw(screen):
        font = pygame.font.Font(None, 50)
        text = font.render("Hello, Pygame!", True, (255, 204, 0))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (255, 204, 0), (text_x - 10, text_y - 10,
                                                 text_w + 20, text_h + 20), 1)


    def draw_square(screen):
        color = pygame.Color(50, 150, 50)
        pygame.draw.rect(screen, color,
                         (20, 20, 100, 100), 0)
        hsv = color.hsva
        color.hsva = (hsv[0], hsv[1], hsv[2] + 30, hsv[3])
        pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)

    def draw_pix(screen):
        for i in range(1):
            screen.fill(pygame.Color('black'),
                        pygame.Rect(random.randint(0, 800), random.randint(0, 600), 2, 2))

    draw(screen)
    draw_square(screen)
    draw_pix(screen)

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


