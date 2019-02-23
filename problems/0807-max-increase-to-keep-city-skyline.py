from typing import List
import unittest


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_row = []
        max_col = []
        for r in grid:
            max_row.append(max(r))
        cols = len(grid[0])
        for j in range(cols):
            highest = -1
            for r in grid:
                if r[j] > highest:
                    highest = r[j]
            max_col.append(highest)
        total = 0
        for i, r in enumerate(grid):
            for j, e in enumerate(r):
                lowest = min(max_row[i], max_col[j])
                total += lowest - e
        return total


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        data = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
        output = 35
        self.assertEqual(Solution().maxIncreaseKeepingSkyline(data), output)


if __name__ == '__main__':
    unittest.main()
