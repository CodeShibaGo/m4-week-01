import unittest
import io
import sys
from mission_03 import print_odd_numbers  # 假設 print_odd_numbers 函式在 mission_03 模組中

class TestPrintOddNumbers(unittest.TestCase):
    def setUp(self):
        # 在每個測試之前捕獲標準輸出
        self.held_output = io.StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # 在每個測試之後恢復標準輸出
        self.held_output.close()
        sys.stdout = sys.__stdout__

    def test_print_odd_numbers(self):
        # 生成期望的輸出：1到100之間的所有奇數
        expected_output = '\n'.join(str(num) for num in range(1, 101, 2)) + '\n'

        print_odd_numbers()  # 調用函式
        actual_output = self.held_output.getvalue()  # 獲取實際輸出

        self.assertEqual(actual_output, expected_output)  # 斷言期望和實際輸出相等

if __name__ == "__main__":
    unittest.main()