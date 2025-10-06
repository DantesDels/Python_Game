import json
import os
import unittest
from src.save import save_game, load_game

class TestSaveLoad(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_save.json'
        self.test_data = {
            "player_name": "Survivant",
            "day": 5,
            "hunger": 30,
            "thirst": 40,
            "energy": 50
        }

    def test_save_game(self):
        save_game(self.test_data, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_load_game(self):
        save_game(self.test_data, self.test_file)
        loaded_data = load_game(self.test_file)
        self.assertEqual(loaded_data, self.test_data)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()