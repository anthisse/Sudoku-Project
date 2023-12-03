import pygame
from sys import exit
# Constants that control fonts and the window size
from gui_constants import *


# Draw the main menu screen
def draw_main_menu(screen):
    title_font = pygame.font.Font(None, 80)
    subtitle_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 30)

    # Draw title information
    title_surface = title_font.render("Welcome to Sudoku!", 1, BLACK)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # Draw subtitle information
    subtitle_surface = subtitle_font.render("Select Difficulty:", 1, BLACK)
    subtitle_rectangle = subtitle_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(subtitle_surface, subtitle_rectangle)

    # Initialize buttons and text
    easy_text = button_font.render("EASY", 1, WHITE)
    medium_text = button_font.render("MEDIUM", 1, WHITE)
    hard_text = button_font.render("HARD", 1, WHITE)
    quit_text = button_font.render("QUIT", 1, WHITE)

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

    # Initialize quit button background color and text
    quit_surface = pygame.Surface((hard_text.get_size()[0] + 60, hard_text.get_size()[1] + 30))
    quit_surface.fill(BLACK)
    quit_surface.blit(quit_text, (35, 15))

    # Initialize button rectangles
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2 - 150, HEIGHT // 2 + 100))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2 + 150, HEIGHT // 2 + 100))
    quit_rectangle = quit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 225))

    # Draw the buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)
    screen.blit(quit_surface, quit_rectangle)

    # Update the display
    while True:
        # For each event
        for event in pygame.event.get():
            # If the event is quit, call sys.exit with code 0
            if event.type == pygame.QUIT:
                exit(0)
            # Otherwise, check what the mouse is doing
            # TODO return a var that controls difficulty
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    print("Easy button clicked!")
                    # return 0
                if medium_rectangle.collidepoint(event.pos):
                    print("Medium button clicked!")
                    # return 1
                if hard_rectangle.collidepoint(event.pos):
                    print("Hard button clicked!")
                    # return 2
                # If the quit button is clicked, exit with success code 0
                if quit_rectangle.collidepoint(event.pos):
                    print("Quit button clicked! Exiting.")
                    exit(0)

        # Update the screen
        pygame.display.update()


# Driver program
def main():
    # Initialize pygame Set the window size, caption, and background image
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    menu_background = pygame.image.load('sudoku_background.jpg').convert()
    menu_background = pygame.transform.smoothscale(menu_background, screen.get_size())

    # Draw the main menu
    screen.blit(menu_background, (0, 0))
    draw_main_menu(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)


if __name__ == "__main__":
    main()
