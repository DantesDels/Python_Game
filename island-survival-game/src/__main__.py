from player import Player
from game import Game

def main():
    player = Player("Survivant")
    game = Game(player)
    game.start()
    

if __name__ == "__main__":
    main()  