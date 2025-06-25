# pet.py
class Pet:
    def __init__(self):
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.cleanliness = 50
        self.is_alive = True

    def feed(self):
        """Increase hunger (decrease hunger level)."""
        self.hunger = min(self.hunger + 10, 100)  # Feeding increases hunger by 10, max 100

    def play(self):
        """Increase happiness (decrease boredom)."""
        self.happiness = min(self.happiness + 10, 100)  # Playing increases happiness

    def clean(self):
        """Increase cleanliness."""
        self.cleanliness = min(self.cleanliness + 10, 100)  # Cleaning increases cleanliness

    def sleep(self):
        """Increase energy (decrease tiredness)."""
        self.energy = min(self.energy + 10, 100)  # Sleeping increases energy

    def update(self):
        """Check if pet is alive based on stats."""
        if self.hunger <= 0 or self.happiness <= 0 or self.energy <= 0 or self.cleanliness <= 0:
            self.is_alive = False
