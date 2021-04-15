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
    @patch('builtins.input')
    def test_calculation2(self,mock_input):
        mock_input.return_value= '10000000'
        self.assertEqual(test(),1497300)
    @patch('builtins.input')
    def test_calculation3(self,mock_input):
        mock_input.return_value= '1200000'
        self.assertEqual(test(),160500)
    @patch('builtins.input')
    def test_calculation4(self,mock_input):
        mock_input.return_value= '120000'
        self.assertEqual(test(),0)  
    @patch('builtins.input')
    def test_calculation5(self,mock_input):
        mock_input.return_value= '150000' 
        self.assertEqual(test(),210)   
    @patch('builtins.input')
    def test_calculation6(self,mock_input):
        mock_input.return_value= '250700'
        self.assertEqual(test(),4616) 
    @patch('builtins.input')
    def test_calculation7(self,mock_input):
        mock_input.return_value= '1350000'
        self.assertEqual(test(),186000) 
    @patch('builtins.input')
    def test_calculation8(self,mock_input):
        mock_input.return_value= '2450000'
        self.assertEqual(test(),364800) 
    @patch('builtins.input')
    def test_calculation9(self,mock_input):
        mock_input.return_value= '3859000'
        self.assertEqual(test(),576150) 
    @patch('builtins.input')
    def test_calculation10(self,mock_input):
        mock_input.return_value= '2468000'
        self.assertEqual(test(),367500) 
    @patch('builtins.input')
    def test_calculation11(self,mock_input):
        mock_input.return_value= '123400'
        self.assertEqual(test(),0) 
    @patch('builtins.input')
    def test_calculation12(self,mock_input):
        mock_input.return_value= '139400'
        self.assertEqual(test(),8) 
    @patch('builtins.input')
    def test_calculation13(self,mock_input):
        mock_input.return_value= '100'
        self.assertEqual(test(),0) 
    @patch('builtins.input')
    def test_calculation14(self,mock_input):
        mock_input.return_value= '142800'
        self.assertEqual(test(),73) 
    @patch('builtins.input')
    def test_calculation15(self,mock_input):
        mock_input.return_value= '300'
        self.assertEqual(test(),0) 
    @patch('builtins.input')
    def test_calculation16(self,mock_input):
        mock_input.return_value= '9860000'
        self.assertEqual(test(),1476300) 
    @patch('builtins.input')
    def test_calculation17(self,mock_input):
        mock_input.return_value= '900000'
        self.assertEqual(test(),109500) 
    @patch('builtins.input')
    def test_calculation18(self,mock_input):
        mock_input.return_value= '570000'
        self.assertEqual(test(),53400) 
    @patch('builtins.input')
    def test_calculation19(self,mock_input):
        mock_input.return_value= '2330000'
        self.assertEqual(test(),346800)
    @patch('builtins.input')
    def test_calculation20(self,mock_input):
        mock_input.return_value= '999999999'
        self.assertEqual(test(),149997299) 
    @patch('builtins.input')
    def test_calculation21(self,mock_input):
        mock_input.return_value= '1'
        self.assertEqual(test(),0) 
    
if __name__ == '__main__':
    unittest.main()
        