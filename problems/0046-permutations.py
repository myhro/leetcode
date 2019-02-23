from typing import List
import unittest


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        tmp = []
        n = len(nums)
        for i in range(n):
            remaining = nums[:i] + nums[i+1:]
            for p in self.permute(remaining):
                tmp.append([nums[i]] + p)
        return tmp


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        data = [1, 2, 3]
        output = [
          [1, 2, 3],
          [1, 3, 2],
          [2, 1, 3],
          [2, 3, 1],
          [3, 1, 2],
          [3, 2, 1],
        ]
        self.assertEqual(Solution().permute(data), output)


if __name__ == '__main__':
    unittest.main()
