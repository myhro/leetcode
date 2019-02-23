import unittest


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        data = ["h", "e", "l", "l", "o"]
        output = ["o", "l", "l", "e", "h"]
        Solution().reverseString(data)
        self.assertEqual(data, output)

    def test_2(self):
        data = ["H", "a", "n", "n", "a", "h"]
        output = ["h", "a", "n", "n", "a", "H"]
        Solution().reverseString(data)
        self.assertEqual(data, output)


if __name__ == '__main__':
    unittest.main()
