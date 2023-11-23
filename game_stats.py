import json

class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        self.initialize_high_score()

    def initialize_high_score(self):
        try:
            with open('save.json') as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
                self.high_score = 0

    def reset_stats(self):
        """Initilize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1