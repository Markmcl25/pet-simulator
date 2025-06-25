# game.py
import pygame
import sys
from pet import Pet  # Import the Pet class

# 1. Initialize pygame
pygame.init()

# 2. Set up the game window
screen = pygame.display.set_mode((800, 600))  # 800x600 window
pygame.display.set_caption("Pet Simulator")

# 3. Set up the clock to control frame rate
clock = pygame.time.Clock()

# 4. Create a pet object
pet = Pet()

# 5. Game loop
running = True
while running:
    # 6. Handle events (key presses, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 7. Fill the screen with a color (white in this case)
    screen.fill((255, 255, 255))  # RGB color for white

    # 8. Display pet stats on the screen
    font = pygame.font.Font(None, 36)

    hunger_text = font.render(f"Hunger: {pet.hunger}", True, (0, 0, 0))
    happiness_text = font.render(f"Happiness: {pet.happiness}", True, (0, 0, 0))
    energy_text = font.render(f"Energy: {pet.energy}", True, (0, 0, 0))
    cleanliness_text = font.render(f"Cleanliness: {pet.cleanliness}", True, (0, 0, 0))

    # Display text on the screen
    screen.blit(hunger_text, (10, 10))
    screen.blit(happiness_text, (10, 50))
    screen.blit(energy_text, (10, 90))
    screen.blit(cleanliness_text, (10, 130))

    # 9. Display "Game Over" message if pet is dead
    if not pet.is_alive:
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(game_over_text, (350, 250))

    # 10. Create Rects for interaction buttons (feed, play, clean)
    feed_button = pygame.Rect(100, 500, 100, 50)
    play_button = pygame.Rect(300, 500, 100, 50)

    # Draw buttons
    pygame.draw.rect(screen, (0, 255, 0), feed_button)  # Feed button (green)
    pygame.draw.rect(screen, (0, 0, 255), play_button)  # Play button (blue)

    # Add text to the buttons
    feed_text = font.render("Feed", True, (0, 0, 0))
    play_text = font.render("Play", True, (0, 0, 0))
    screen.blit(feed_text, (120, 510))
    screen.blit(play_text, (320, 510))

    # 11. Handle button clicks
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if feed_button.collidepoint(x, y):
            pet.feed()
        elif play_button.collidepoint(x, y):
            pet.play()

    # 12. Update pet stats over time
    pet.update()

    # 13. Update the display
    pygame.display.flip()

    # 14. Set the frame rate (60 FPS)
    clock.tick(60)

# 15. Quit pygame when the game loop ends
pygame.quit()
sys.exit()
