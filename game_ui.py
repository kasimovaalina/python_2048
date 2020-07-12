import game_logic
import pygame

# используемые цвета
ALMOST_WHITE = (216, 201, 220)
LIGHT_PURPLE = (117, 82, 126)
BACK_COLOR = (104, 47, 90)
# начальные координаты для отрисовки плиток
x = 40
y = 40
# ширина одной плитки вместе с отступом
step = 98

class Pygame_helper:
    instruction1 = "Use  arrow keys to move the tiles."
    instruction2 = "When two tiles with the same number touch, "
    instruction3 = "they merge into one!"
    instruction4 = "Press N to start new game anytime."

    # метод отрисовки окна, информирующее пользователя о выигрыше, содержит в себе дальнейшие инструкции
    def draw_congrats(self, screen):
        congrats_pic = pygame.image.load("winner_congrats.bmp")
        screen.blit(congrats_pic, (0, 0))

    def draw_gameover(self, screen):
        gameover_pic = pygame.image.load("game_over.bmp")
        screen.blit(gameover_pic, (0, 0))

    # метод отрисовки массива/плиток
    def draw_grid(self, screen, grid):
        for i in range(4):
            for j in range(4):
                if grid[i][j] != 0:
                    new_x = x + j * step
                    new_y = y + i * step
                    pygame.draw.rect(screen, ALMOST_WHITE, (new_x, new_y, 93, 93))
                    if grid[i][j] < 10:
                        nmbr = str(grid[i][j])
                        nmbr_font = pygame.font.SysFont('comicsansms', 48)
                        nmbr_text = nmbr_font.render(nmbr, 1, BACK_COLOR)
                        screen.blit(nmbr_text, (new_x + 30, new_y + 10))
                    elif grid[i][j] < 20:
                        nmbr = " " + str(grid[i][j])
                        nmbr_font = pygame.font.SysFont('comicsansms', 48)
                        nmbr_text = nmbr_font.render(nmbr, 1, BACK_COLOR)
                        screen.blit(nmbr_text, (new_x + 10, new_y + 10))
                    elif grid[i][j] < 100:
                        nmbr = str(grid[i][j])
                        nmbr_font = pygame.font.SysFont('comicsansms', 48)
                        nmbr_text = nmbr_font.render(nmbr, 1, BACK_COLOR)
                        screen.blit(nmbr_text, (new_x + 15, new_y + 10))
                    elif grid[i][j] < 1000:
                        nmbr = str(grid[i][j])
                        nmbr_font = pygame.font.SysFont('comicsansms', 43)
                        nmbr_text = nmbr_font.render(nmbr, 1, BACK_COLOR)
                        screen.blit(nmbr_text, (new_x + 10, new_y + 10))
                    elif grid[i][j] < 10000:
                        nmbr = str(grid[i][j])
                        nmbr_font = pygame.font.SysFont('comicsansms', 37)
                        nmbr_text = nmbr_font.render(nmbr, 1, BACK_COLOR)
                        screen.blit(nmbr_text, (new_x, new_y + 20))

    # метод отрисовки пустых плиток, часть фона
    def draw_background_cells(self, screen):
        for i in range(4):
            for j in range(4):
                new_x = x + j * step
                new_y = y + i * step
                pygame.draw.rect(screen, LIGHT_PURPLE, (new_x, new_y, 93, 93))

    # метод фона с текстовыми инструкциями
    def draw_background(self, screen):
        instruction_font = pygame.font.SysFont('comicsansms', 18)
        pygame.draw.rect(screen, BACK_COLOR, (0, 0, 470, 600))
        self.draw_background_cells(screen)
        instruction_text1 = instruction_font.render(self.instruction1, 1, ALMOST_WHITE)
        instruction_text2 = instruction_font.render(self.instruction2, 1, ALMOST_WHITE)
        instruction_text3 = instruction_font.render(self.instruction3, 1, ALMOST_WHITE)
        instruction_text4 = instruction_font.render(self.instruction4, 1, ALMOST_WHITE)
        screen.blit(instruction_text1, (39, 478))
        screen.blit(instruction_text2, (39, 501))
        screen.blit(instruction_text3, (39, 524))
        screen.blit(instruction_text4, (39, 547))

    # главная функция, содержащая в себе игровой цикл
    def start(self, screen, game: game_logic.Game_core):
        keep_going = True
        clock = pygame.time.Clock()
        play_after_2048 = False
        changed_DOWN = True
        changed_RIGHT = True
        changed_UP = True
        changed_LEFT = True
        while keep_going:
            reached_2048 = game.is_2048_in_grid()
            self.draw_background(screen)
            self.draw_grid(screen, game.grid)
            # цикл обработки нажатий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keep_going = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        grid_copy = game.make_grid_copy()
                        game.move_tiles(game_logic.Direction.DOWN)
                        changed_DOWN = game.is_grid_changed(grid_copy)
                    elif event.key == pygame.K_RIGHT:
                        grid_copy = game.make_grid_copy()
                        game.move_tiles(game_logic.Direction.RIGHT)
                        changed_RIGHT = game.is_grid_changed(grid_copy)
                    elif event.key == pygame.K_UP:
                        grid_copy = game.make_grid_copy()
                        game.move_tiles(game_logic.Direction.UP)
                        changed_UP = game.is_grid_changed(grid_copy)
                    elif event.key == pygame.K_LEFT:
                        grid_copy = game.make_grid_copy()
                        game.move_tiles(game_logic.Direction.LEFT)
                        changed_LEFT = game.is_grid_changed(grid_copy)
                    elif event.key == pygame.K_n:
                        game.create_newgame()
            # если пользователь попытался сдвинуть плитки во все четрые стороны,
            # но ничего не изменилось,
            # значит доска полная и ходов больше не осталось
            if (not changed_DOWN and not changed_LEFT and not changed_RIGHT and not changed_UP):
                self.draw_gameover(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        keep_going = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_n:
                            game.create_newgame()
                            changed_DOWN = True
                            changed_RIGHT = True
                            changed_UP = True
                            changed_LEFT = True
            # если пользователь получил в процессе игры 2048,
            # будет отрисовано окно с поздравлением
            # программа так же будет ожидать событие с клавиатуры, на тот
            # случай если пользователь захочет начать новую игру
            # или продолжить играть дальше
            if reached_2048 and not play_after_2048:
                self.draw_congrats(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        keep_going = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_n:
                            game.create_newgame()
                        elif event.key == pygame.K_c:
                            play_after_2048 = True
            pygame.display.update()
            clock.tick(60)
