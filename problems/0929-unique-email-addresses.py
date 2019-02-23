from typing import List
import unittest


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq = set()
        for e in emails:
            name, domain = e.split('@')
            name = name.replace('.', '')
            if '+' in name:
                plus = name.index('+')
                name = name[:plus]
            uniq.add(name + '@' + domain)
        return len(uniq)


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        data = [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ]
        output = 2
        self.assertEqual(Solution().numUniqueEmails(data), output)


if __name__ == '__main__':
    unittest.main()
