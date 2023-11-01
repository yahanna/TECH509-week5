import unittest
import logic
from logic import get_winner,other_player,make_empty_board

class TestLogic(unittest.TestCase):

    def test_get_winner_X(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def test_get_winner_O(self):
        board = [
            ['O', 'O', 'X'],
            [None, 'O', 'O'],
            ['X', 'X', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')

    # def test_no_winner(self):

    #     board = [
    #         ['X', 'O', 'X'],
    #         ['O', 'X', 'O'],
    #         ['X', 'X', 'O'],
    #     ]
    #     self.assertIsNone(logic.get_winner(board))
         
    def test_other_player(self):
        self.assertEqual(logic.other_player('X'), 'O')
        self.assertEqual(logic.other_player('O'), 'X')

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()

