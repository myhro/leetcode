from typing import List
import copy
import unittest


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    def __init__(self):
        self.board = [[]]
        self.cols = 0
        self.rows = 0

    def count_neighbors(self, x, y):
        neighbors = 0
        border_top = x == 0
        border_bottom = x == (self.rows - 1)
        border_left = y == 0
        border_right = y == (self.cols - 1)
        top = Point(x - 1, y - 1)
        bottom = Point(x + 1, y + 1)
        if border_top:
            top.x = x
        if border_left:
            top.y = y
        if border_right:
            bottom.y = y
        if border_bottom:
            bottom.x = x
        for i in range(top.x, bottom.x + 1):
            for j in range(top.y, bottom.y + 1):
                if i == x and j == y:
                    continue
                neighbors += self.board[i][j]
        return neighbors

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = copy.deepcopy(board)
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        for i in range(self.rows):
            for j in range(self.cols):
                neighbors = self.count_neighbors(i, j)
                if board[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        board[i][j] = 0
                else:
                    if neighbors == 3:
                        board[i][j] = 1


class SolutionTestCase(unittest.TestCase):
    def test_example(self):
        board = [
          [0, 1, 0],
          [0, 0, 1],
          [1, 1, 1],
          [0, 0, 0],
        ]
        expected = [
          [0, 0, 0],
          [1, 0, 1],
          [0, 1, 1],
          [0, 1, 0]
        ]
        s = Solution()
        s.gameOfLife(board)
        for i in range(s.rows):
            self.assertCountEqual(board[i], expected[i])


if __name__ == '__main__':
    unittest.main()
