import unittest

null = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insert(root, node):
    if node.val is None:
        return None
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def new_tree(data):
    root = TreeNode(data.pop(0))
    for i in data:
        insert(root, TreeNode(i))
    return root


def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    print(root.val)
    print_tree(root.right)


class Solution:
    def __init__(self):
        self.total = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return
        if root.val >= L and root.val <= R:
            self.total += root.val
        self.rangeSumBST(root.left, L, R)
        self.rangeSumBST(root.right, L, R)
        return self.total


class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        data = [10, 5, 15, 3, 7, null, 18]
        root = new_tree(data)
        left = 7
        right = 15
        output = 32
        self.assertEqual(Solution().rangeSumBST(root, left, right), output)

    def test_2(self):
        data = [10, 5, 15, 3, 7, 13, 18, 1, null, 6]
        root = new_tree(data)
        left = 6
        right = 10
        output = 23
        self.assertEqual(Solution().rangeSumBST(root, left, right), output)


if __name__ == '__main__':
    unittest.main()
