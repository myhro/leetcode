import unittest


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                r.append("FizzBuzz")
            elif i % 3 == 0:
                r.append("Fizz")
            elif i % 5 == 0:
                r.append("Buzz")
            else:
                r.append(str(i))
        return r


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        data = 15
        output = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ]
        self.assertEqual(Solution().fizzBuzz(data), output)


if __name__ == '__main__':
    unittest.main()
