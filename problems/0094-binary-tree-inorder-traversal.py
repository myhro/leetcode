import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_tree(root):
    if root is None:
        print('null')
        return
    print_tree(root.left)
    print(root.val)
    print_tree(root.right)


class Solution(object):
    def __init__(self):
        self.r = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return self.r
        self.inorderTraversal(root.left)
        self.r.append(root.val)
        self.inorderTraversal(root.right)
        return self.r


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        output = [1, 3, 2]
        self.assertEqual(Solution().inorderTraversal(root), output)


if __name__ == '__main__':
    unittest.main()
