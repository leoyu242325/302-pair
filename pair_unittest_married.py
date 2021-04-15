import unittest
from unittest.mock import patch
from married_test import test
class test_single(unittest.TestCase):
    @patch('builtins.input')
    def test_calculation1(self,mock_input):
        mock_input.side_effect = ['125000','158000']
        self.assertEqual(test(),97)
    @patch('builtins.input')
    def test_calculation2(self,mock_input):
        mock_input.side_effect = ['190000','230000']
        self.assertEqual(test(),4160)
    @patch('builtins.input')
    def test_calculation3(self,mock_input):
        mock_input.side_effect = ['2140000','120000']
        self.assertEqual(test(),317240)
    @patch('builtins.input')
    def test_calculation4(self,mock_input):
        mock_input.side_effect = ['1700000','14389000']
        self.assertEqual(test(),2401150)
    @patch('builtins.input')
    def test_calculation5(self,mock_input):
        mock_input.side_effect = ['140000','100000']
        self.assertEqual(test(),0)
    @patch('builtins.input')
    def test_calculation6(self,mock_input):
        mock_input.side_effect = ['2900000','2000000']
        self.assertEqual(test(),728800)
    @patch('builtins.input')
    def test_calculation7(self,mock_input):
        mock_input.side_effect = ['40000','600000']
        self.assertEqual(test(),42520)
    @patch('builtins.input')
    def test_calculation8(self,mock_input):
        mock_input.side_effect = ['1800000','700000']
        self.assertEqual(test(),338000)
    @patch('builtins.input')
    def test_calculation9(self,mock_input):
        mock_input.side_effect = ['2330000','400000']
        self.assertEqual(test(),371300)
    @patch('builtins.input')
    def test_calculation10(self,mock_input):
        mock_input.side_effect = ['1000000','100000']
        self.assertEqual(test(),120210)
    @patch('builtins.input')
    def test_calculation11(self,mock_input):
        mock_input.side_effect = ['200000','300000']
        self.assertEqual(test(),10900)
    @patch('builtins.input')
    def test_calculation12(self,mock_input):
        mock_input.side_effect = ['2800000','260000']
        self.assertEqual(test(),422800)
    @patch('builtins.input')
    def test_calculation13(self,mock_input):
        mock_input.side_effect = ['600000','60000']
        self.assertEqual(test(),45750)
    @patch('builtins.input')
    def test_calculation14(self,mock_input):
        mock_input.side_effect = ['780000','960000']
        self.assertEqual(test(),208800)
    @patch('builtins.input')
    def test_calculation15(self,mock_input):
        mock_input.side_effect = ['1000000','1059000']
        self.assertEqual(test(),263030)
    @patch('builtins.input')
    def test_calculation16(self,mock_input):
        mock_input.side_effect = ['2970000','158000']
        self.assertEqual(test(),443162)
    @patch('builtins.input')
    def test_calculation17(self,mock_input):
        mock_input.side_effect = ['700000','958000']
        self.assertEqual(test(),194860)
    @patch('builtins.input')
    def test_calculation18(self,mock_input):
        mock_input.side_effect = ['400000','709000']
        self.assertEqual(test(),101530)
    @patch('builtins.input')
    def test_calculation19(self,mock_input):
        mock_input.side_effect = ['821920','910200']
        self.assertEqual(test(),207460)
    @patch('builtins.input')
    def test_calculation20(self,mock_input):
        mock_input.side_effect = ['448000','500000']
        self.assertEqual(test(),74160)
    @patch('builtins.input')
    def test_calculation21(self,mock_input):
        mock_input.side_effect = ['432890','290394']
        self.assertEqual(test(),38478)
    @patch('builtins.input')
    def test_calculation22(self,mock_input):
        mock_input.side_effect = ['742000','372900']
        self.assertEqual(test(),102533)
    @patch('builtins.input')
    def test_calculation23(self,mock_input):
        mock_input.side_effect = ['620000','620000']
        self.assertEqual(test(),123800)
    @patch('builtins.input')
    def test_calculation24(self,mock_input):
        mock_input.side_effect = ['349000','268300']
        self.assertEqual(test(),22225)
    @patch('builtins.input')
    def test_calculation25(self,mock_input):
        mock_input.side_effect = ['1700000','4389000']
        self.assertEqual(test(),901150)
    @patch('builtins.input')
    def test_calculation26(self,mock_input):
        mock_input.side_effect = ['138948','10']
        self.assertEqual(test(),0)
    
if __name__ == '__main__':
    unittest.main()