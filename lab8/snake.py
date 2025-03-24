import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20  # Grid size

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake initial setup
snake = [(100, 100), (80, 100), (60, 100)]  # Starting snake body
snake_dir = (CELL_SIZE, 0)  # Initial movement direction

# Generate food in a random position avoiding the snake
def generate_food():
    while True:
        food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
        if food not in snake:
            return food

food = generate_food()

# Game variables
running = True
clock = pygame.time.Clock()
speed = 10  # Initial speed
score = 0
level = 1
font = pygame.font.Font(None, 36)

# Main game loop
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Snake movement control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
        snake_dir = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
        snake_dir = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
        snake_dir = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
        snake_dir = (CELL_SIZE, 0)
    
    # Move the snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    # Check wall collision
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False  # Game over on wall collision
    
    # Check self-collision
    if new_head in snake:
        running = False  # Game over if snake runs into itself
    
    # Add new head
    snake.insert(0, new_head)
    
    # Check if food is eaten
    if new_head == food:
        score += 1
        food = generate_food()
        
        # Level up every 3 food items
        if score % 3 == 0:
            level += 1
            speed += 2  # Increase speed
    else:
        snake.pop()  # Remove tail if no food eaten
    
    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    
    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    
    # Display score and level
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    
    # Refresh screen
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
