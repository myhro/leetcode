import unittest


class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        data = "Hello"
        output = "hello"
        self.assertEqual(Solution().toLowerCase(data), output)

    def test_2(self):
        data = "here"
        output = "here"
        self.assertEqual(Solution().toLowerCase(data), output)

    def test_3(self):
        data = "LOVELY"
        output = "lovely"
        self.assertEqual(Solution().toLowerCase(data), output)


if __name__ == '__main__':
    unittest.main()
