import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))  # 800x600 window
pygame.display.set_caption("Pet Simulator")

class Pet:
    def __init__(self):
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.cleanliness = 50
        self.is_alive = True

    def feed(self):
        self.hunger = min(self.hunger + 10, 100)  # Feeding increases hunger by 10, max 100

    def play(self):
        self.happiness = min(self.happiness + 10, 100)  # Playing increases happiness

    def clean(self):
        self.cleanliness = min(self.cleanliness + 10, 100)  # Cleaning increases cleanliness

    def sleep(self):
        self.energy = min(self.energy + 10, 100)  # Sleeping increases energy

    def update(self):
        # Check if pet is alive based on stats
        if self.hunger <= 0 or self.happiness <= 0 or self.energy <= 0 or self.cleanliness <= 0:
            self.is_alive = False

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
