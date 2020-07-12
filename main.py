import game_ui
import game_logic
import pygame

def main():
    game = game_logic.Entrails()
    game.create_newgame()
    pygame.init()
    pygame.display.set_caption('2048')
    screen = pygame.display.set_mode([470, 600])
    game_visual = game_ui.Externals()
    game_visual.start(screen, game)
    pygame.quit

if __name__ == "__main__":
    main()
