from typing import List
import unittest


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                j = i
                while j < (n - 1) and nums[j] == 0:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        data = [0, 1, 0, 3, 12]
        output = [1, 3, 12, 0, 0]
        Solution().moveZeroes(data)
        self.assertEqual(data, output)

    def test_2(self):
        data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        output = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        Solution().moveZeroes(data)
        self.assertEqual(data, output)

    def test_3(self):
        data = [0]
        output = [0]
        Solution().moveZeroes(data)
        self.assertEqual(data, output)


if __name__ == '__main__':
    unittest.main()
