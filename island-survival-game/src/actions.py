def fish(player):
    player.hunger -= 10
    player.energy -= 5
    return "You went fishing and caught some food!"

def search_water(player):
    player.thirst -= 10
    player.energy -= 5
    return "You searched for water and found a source!"

def sleep(player):
    player.energy += 15
    player.thirst += 5
    player.hunger += 5
    return "You took a rest and regained some energy!"

def explore(player):
   pass  # Implementation of explore action