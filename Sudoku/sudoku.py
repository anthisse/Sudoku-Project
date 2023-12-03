# TODO This clutters the namespace
import pygame
import sys
from gui_constants import *


def draw_main_menu(screen):
    title_font = pygame.font.Font(None, 80)
    subtitle_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 30)

    # TODO change background to image instead of solid color
    screen.fill(BG_COLOR)

    # Draw title information
    title_surface = title_font.render("Welcome to Sudoku!", 1, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # Draw subtitle information
    subtitle_surface = subtitle_font.render("Select Difficulty:", 1, LINE_COLOR)
    subtitle_rectangle = subtitle_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(subtitle_surface, subtitle_rectangle)

    # Initialize buttons and text
    easy_text = button_font.render("EASY", 1, (255, 255, 255))
    medium_text = button_font.render("MEDIUM", 1, (255, 255, 255))
    hard_text = button_font.render("HARD", 1, (255, 255, 255))

    # Initialize easy button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 60, easy_text.get_size()[1] + 30))
    easy_surface.fill(GREEN)
    easy_surface.blit(easy_text, (30, 15))

    # Initialize medium button background color and text
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 60, medium_text.get_size()[1] + 30))
    medium_surface.fill(YELLOW)
    medium_surface.blit(medium_text, (30, 15))

    # Initialize hard button background color and text
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 60, hard_text.get_size()[1] + 30))
    hard_surface.fill(RED)
    hard_surface.blit(hard_text, (30, 15))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2 - 150, HEIGHT // 2 + 100))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2 + 150, HEIGHT // 2 + 100))

    # Draw the buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.display.update()

# Driver program
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    draw_main_menu(screen)

    pygame.display.set_caption("Sudoku")
    screen.fill(BG_COLOR)

if __name__ == "__main__":
    main()
