import logical_part
import pygame

ALMOST_WHITE = (216, 201, 220)
LIGHT_PURPLE = (117, 82, 126)
GREEN = (0, 225, 0)
class Externals:
    BACK_COLOR = (104, 47, 90)
    instruction1 = "Use WASD to move the tiles."
    instruction2 = "When two tiles with the same number touch, "
    instruction3 = "they merge into one!"

    def draw_grid(self, screen, grid):
        x = 40
        y = 40
        step = 98
        for i in range(4):
            for j in range(4):
                if grid[i][j] != 0:
                    new_x = x + i * step
                    new_y = y + j * step
                    pygame.draw.rect(screen, ALMOST_WHITE, (new_x, new_y, 93, 93))
                    if grid[i][j] < 10:
                        nmbr = str(grid[i][j])
                        nmbr_font = pygame.font.SysFont('comicsansms', 48)
                        nmbr_text = nmbr_font.render(nmbr, 1, self.BACK_COLOR)
                        screen.blit(nmbr_text, (new_x + 30, new_y + 10))

    def draw_background_cells(self, screen):
        pygame.draw.rect(screen, LIGHT_PURPLE, (40, 40, 93, 93))
        pygame.draw.rect(screen, LIGHT_PURPLE, (40, 40 + 98, 93, 93))
        pygame.draw.rect(screen, LIGHT_PURPLE, (40, 40 + 98 + 98, 93, 93))
        pygame.draw.rect(screen, LIGHT_PURPLE, (40, 40 + 98 * 3, 93, 93))
        pygame.draw.rect(screen, LIGHT_PURPLE, (40 + 98, 40, 93, 93))
        pygame.draw.rect(screen, LIGHT_PURPLE, (40 + 98, 40 + 98, 93, 93))
        pygame.draw.rect(screen, LIGHT_PURPLE, (40 + 98, 40 + 98 + 98, 93, 93))
        pygame.draw.rect(screen, LIGHT_PURPLE, (40 + 98, 40 + 98 * 3, 93, 93))
        pygame.draw.rect(screen, LIGHT_PURPLE, (40 + 98 + 98, 40, 93, 93))
        pygame.draw.rect(screen, LIGHT_PURPLE, (40 + 98 + 98, 40 + 98, 93, 93))
        pygame.draw.rect(screen, LIGHT_PURPLE, (40 + 98 + 98, 40 + 98 + 98, 93, 93))
        pygame.draw.rect(screen, LIGHT_PURPLE, (40 + 98 + 98, 40 + 98 * 3, 93, 93))
        pygame.draw.rect(screen, LIGHT_PURPLE, (40 + 98 + 98 + 98, 40, 93, 93))
        pygame.draw.rect(screen, LIGHT_PURPLE, (40 + 98 + 98 + 98, 40 + 98, 93, 93))
        pygame.draw.rect(screen, LIGHT_PURPLE, (40 + 98 + 98 + 98, 40 + 98 + 98, 93, 93))
        pygame.draw.rect(screen, LIGHT_PURPLE, (40 + 98 + 98 + 98, 40 + 98 * 3, 93, 93))

    def draw_background(self, screen):
        instruction_font = pygame.font.SysFont('comicsansms', 18)
        pygame.draw.rect(screen, self.BACK_COLOR, (0, 0, 470, 600))
        self.draw_background_cells(screen)
        instruction_text1 = instruction_font.render(self.instruction1, 1, ALMOST_WHITE)
        instruction_text2 = instruction_font.render(self.instruction2, 1, ALMOST_WHITE)
        instruction_text3 = instruction_font.render(self.instruction3, 1, ALMOST_WHITE)
        screen.blit(instruction_text1, (39, 478))
        screen.blit(instruction_text2, (39, 501))
        screen.blit(instruction_text3, (39, 524))

    def start(self, screen, game: logical_part.Entrails):
        keep_going = True
        while keep_going:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keep_going = False
            self.draw_background(screen)
            self.draw_grid(screen, game.grid)
            pygame.display.update()
