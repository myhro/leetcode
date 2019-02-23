import unittest


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniq = set()
        for i in nums:
            if i in uniq:
                uniq.remove(i)
            else:
                uniq.add(i)
        return uniq.pop()


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        data = [2, 2, 1]
        output = 1
        self.assertEqual(Solution().singleNumber(data), output)

    def test_2(self):
        data = [4, 1, 2, 1, 2]
        output = 4
        self.assertEqual(Solution().singleNumber(data), output)


if __name__ == '__main__':
    unittest.main()
