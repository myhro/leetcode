import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        opposite = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if c != opposite[top]:
                    return False
        if len(stack) == 0:
            return True
        return False


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().isValid('()'), True)

    def test_2(self):
        self.assertEqual(Solution().isValid('()[]{}'), True)

    def test_3(self):
        self.assertEqual(Solution().isValid('(]'), False)

    def test_4(self):
        self.assertEqual(Solution().isValid('('), False)

    def test_5(self):
        self.assertEqual(Solution().isValid(')'), False)

    def test_6(self):
        self.assertEqual(Solution().isValid('([)]'), False)


unittest.main()
