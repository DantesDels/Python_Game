import unittest
from src.game import Game
from src.player import Player
from src.actions import Actions
from src.events import Events

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player = Player(name="Survivor")
        self.game = Game(player=self.player)

    def test_initial_resources(self):
        self.assertEqual(self.player.hunger, 0)
        self.assertEqual(self.player.thirst, 0)
        self.assertEqual(self.player.energy, 100)

    def test_action_fishing(self):
        initial_hunger = self.player.hunger
        initial_energy = self.player.energy
        self.game.perform_action(Actions.FISH)
        self.assertGreater(self.player.hunger, initial_hunger)
        self.assertLess(self.player.energy, initial_energy)

    def test_action_searching_water(self):
        initial_thirst = self.player.thirst
        initial_energy = self.player.energy
        self.game.perform_action(Actions.SEARCH_WATER)
        self.assertGreater(self.player.thirst, initial_thirst)
        self.assertLess(self.player.energy, initial_energy)

    def test_action_sleeping(self):
        initial_energy = self.player.energy
        self.game.perform_action(Actions.SLEEP)
        self.assertGreater(self.player.energy, initial_energy)
        self.assertLessEqual(self.player.thirst, 100)
        self.assertLessEqual(self.player.hunger, 100)

    def test_random_event_rain(self):
        self.player.thirst = 90
        Events.trigger_event("rain", self.player)
        self.assertLess(self.player.thirst, 90)

    def test_game_over_hunger(self):
        self.player.hunger = 100
        self.assertTrue(self.game.is_game_over())

    def test_game_over_thirst(self):
        self.player.thirst = 100
        self.assertTrue(self.game.is_game_over())

    def test_game_over_energy(self):
        self.player.energy = 0
        self.assertTrue(self.game.is_game_over())

if __name__ == '__main__':
    unittest.main()