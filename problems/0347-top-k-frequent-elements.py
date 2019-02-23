from typing import List
import heapq
import unittest


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        return heapq.nlargest(k, freq, freq.get)


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        output = [1, 2]
        self.assertEqual(Solution().topKFrequent(nums, k), output)

    def test_2(self):
        nums = [1]
        k = 1
        output = [1]
        self.assertEqual(Solution().topKFrequent(nums, k), output)


if __name__ == '__main__':
    unittest.main()
