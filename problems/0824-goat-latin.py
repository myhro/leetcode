import unittest


class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = []
        words = S.split()
        for i, w in enumerate(words):
            if w[0].lower() not in 'aeiou':
                w = w[1:] + w[0]
            w += 'ma'
            w += 'a' * (i + 1)
            result.append(w)
        return ' '.join(result)


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        data = 'I speak Goat Latin'
        output = 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'
        self.assertEqual(Solution().toGoatLatin(data), output)

    def test_2(self):
        data = 'The quick brown fox jumped over the lazy dog'
        output = 'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa '\
            'overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa'
        self.assertEqual(Solution().toGoatLatin(data), output)


if __name__ == '__main__':
    unittest.main()
