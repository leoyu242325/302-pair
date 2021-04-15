import unittest
from unittest.mock import patch
from married_test import test
class test_single(unittest.TestCase):
    @patch('builtins.input')
    def test_calculation(self,mock_input):
        mock_input.side_effect = ['40000','600000']
        self.assertEqual(test(),42520)
    @patch('builtins.input')
    def test_calculation1(self,mock_input):
        mock_input.side_effect = ['1800000','700000']
        self.assertEqual(test(),338000)
if __name__ == '__main__':
    unittest.main()
        