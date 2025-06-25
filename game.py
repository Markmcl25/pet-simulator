import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))  # 800x600 window
pygame.display.set_caption("Pet Simulator")

# Set up clock to control frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events (key presses, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (white in this case)
    screen.fill((255, 255, 255))  # RGB color for white

    # Game elements here (text, images, buttons)

    # Update the display
    pygame.display.flip()

    # Set the frame rate (60 FPS)
    clock.tick(60)

# Quit pygame when the game loop ends
pygame.quit()
sys.exit()
