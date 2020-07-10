import visual_part
import logical_part
import pygame

def main():
    game = logical_part.Entrails()
    game.create_newgame()
    pygame.init()
    pygame.display.set_caption('2048')
    screen = pygame.display.set_mode([470, 600])
    game_visual = visual_part.Externals()
    game_visual.start(screen, game)
    pygame.quit

if __name__ == "__main__":
    main()
