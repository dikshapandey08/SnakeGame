import pygame
import time
import random

# ✅ Initialize Pygame properly
pygame.init()

# ✅ Initialize the font module explicitly (Fixes the font error)
pygame.font.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set the width and height of the game window
window_width = 800
window_height = 600
window_size = (window_width, window_height)
game_window = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption("Snake Game")

# Set the clock for the game
clock = pygame.time.Clock()

# Set the size of the snake's body segment
segment_size = 20

# Set the speed of the snake
snake_speed = 10

# ✅ Define fonts AFTER initializing Pygame
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def show_score(score):
    score_text = score_font.render("Score: " + str(score), True, WHITE)
    game_window.blit(score_text, [10, 10])

def game_over():
    game_window.fill(BLACK)
    game_over_text = font_style.render("Game Over!", True, RED)
    game_window.blit(game_over_text, [window_width // 3, window_height // 3])
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

def snake_game():
    snake_x = window_width // 2
    snake_y = window_height // 2
    change_in_x = 0
    change_in_y = 0
    snake_body = []
    snake_length = 1

    # Set the initial position of the food
    food_x = round(random.randrange(0, window_width - segment_size) / segment_size) * segment_size
    food_y = round(random.randrange(0, window_height - segment_size) / segment_size) * segment_size

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press Esc to quit
                    pygame.quit()
                    quit()
                if event.key == pygame.K_LEFT and change_in_x == 0:
                    change_in_x = -segment_size
                    change_in_y = 0
                elif event.key == pygame.K_RIGHT and change_in_x == 0:
                    change_in_x = segment_size
                    change_in_y = 0
                elif event.key == pygame.K_UP and change_in_y == 0:
                    change_in_y = -segment_size
                    change_in_x = 0
                elif event.key == pygame.K_DOWN and change_in_y == 0:
                    change_in_y = segment_size
                    change_in_x = 0

        # Move the snake
        snake_x += change_in_x
        snake_y += change_in_y

        # Check for wall collision
        if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
            game_over()

        # Draw everything
        game_window.fill(BLACK)
        pygame.draw.rect(game_window, BLUE, [food_x, food_y, segment_size, segment_size])

        # Update the snake's body
        snake_head = [snake_x, snake_y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Check for self-collision
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_over()

        # Draw the snake
        for segment in snake_body:
            pygame.draw.rect(game_window, GREEN, [segment[0], segment[1], segment_size, segment_size])

        # Check for food collision
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, window_width - segment_size) / segment_size) * segment_size
            food_y = round(random.randrange(0, window_height - segment_size) / segment_size) * segment_size
            snake_length += 1

        # Show score
        show_score(snake_length - 1)

        # Refresh display
        pygame.display.flip()

        # Control game speed
        clock.tick(snake_speed)

# Start the game
snake_game()
