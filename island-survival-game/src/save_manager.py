def save_game(player, day, difficulty):
    saved_data = {
        'player': {
            'name': self.player.name,
            'hunger': self.player.hunger,
            'thirst': self.player.thirst,
            'energy': self.player.energy,
            'days_survived': self.player.days_survived
            },
        'game': {
            'day': self.game.day,
            'difficulty': self.game.difficulty
            }
        }
    print("Game saved successfully!")
    
def load_game():
    loaded_data = {
        'player': {
            'name': self.player.name,
            'hunger': self.player.hunger,
            'thirst': self.player.thirst,
            'energy': self.player.energy,
            'days_survived': self.player.days_survived
            },
        'game': {
            'day': self.game.day,
            'difficulty': self.game.difficulty
            }
        }
    print("Game loaded successfully!")
    return loaded_data