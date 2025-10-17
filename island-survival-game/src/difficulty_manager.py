from player import Player
import json

def dfficulty_manager(difficulty, days_survived):
    difficulty = open('difficulty_multipliers.json', 'r')
    difficulty_data = json.load(difficulty)
    difficulty.close()
    days_survived = Player.self.days_survived
    if difficulty_data.get(difficulty):
        settings = difficulty_data[difficulty]
        Player.self.hunger += settings.get("hunger")
        Player.self.thirst += settings.get("thirst")
        Player.self.energy += settings.get("energy")
         
    else:
        print("Unknown difficulty level. Default settings applied.")
        settings = difficulty_data["Baby"]
        Player.self.hunger += settings.get("hunger")
        Player.self.thirst += settings.get("thirst")
        Player.self.energy += settings.get("energy")
    for days_survived in range(difficulty["days_left"]):
        days_survived += 1
        if days_survived == difficulty["days_left"]:
            break
        else:
            daily_mult_data += settings.get(difficulty["daily_growth"])
        pass
