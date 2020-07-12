import game_ui
import game_logic
import pygame

# точка входа в программу
def main():
    game = game_logic.Game_core()
    game.create_newgame()
    # инициализация окна и старт игры
    pygame.init()
    pygame.display.set_caption('2048')
    screen = pygame.display.set_mode([470, 600])
    game_visual = game_ui.Pygame_helper()
    game_visual.start(screen, game)
    pygame.quit

if __name__ == "__main__":
    main()
