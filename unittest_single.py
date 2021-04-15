import unittest
from unittest.mock import patch
from single_test import test
class test_single(unittest.TestCase):
    @patch('builtins.input')
    def test_calculation(self,mock_input):
        mock_input.return_value= '570000'
        self.assertEqual(test(),53400)
    @patch('builtins.input')
    def test_calculation1(self,mock_input):
        mock_input.return_value= '4800000'
        self.assertEqual(test(),717300)
if __name__ == '__main__':
    unittest.main()
        