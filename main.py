import pygame
import sys
from level import Level
from settings import *
from menu import ImageButton



screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("")
main_background = pygame.image.load("background1.jpeg")


def main_menu():
    start_button = ImageButton(WIDTH/2 - (252/2), 250, 252, 74, "Новая игра", "green_button2_hover.png")
    exit_button = ImageButton(WIDTH/2 - (252/2), 350, 252, 74, "Выход", "green_button2_hover.png")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, -330))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                running = False
                game = Game()
                game.run()


            for btn in [start_button, exit_button]:
                btn.handle_event(event)

        for btn in [start_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


class Game:
    def __init__(self):
        # общая настройка
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('AncientTemple')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    main_menu()