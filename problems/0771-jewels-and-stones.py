import unittest


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        for c in S:
            if c in J:
                total += 1
        return total


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        jewels = 'aA'
        stones = 'aAAbbbb'
        output = 3
        self.assertEqual(Solution().numJewelsInStones(jewels, stones), output)

    def test_2(self):
        jewels = 'z'
        stones = 'ZZ'
        output = 0
        self.assertEqual(Solution().numJewelsInStones(jewels, stones), output)


if __name__ == '__main__':
    unittest.main()
