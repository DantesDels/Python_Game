# Entry point for the island survival game

from player import Player
from game import Game

def main():
    # create a default player and start the game loop
    player = Player("Survivant")    
    game = Game(player) 
    game.start_game()   

if __name__ == "__main__":
    main()  