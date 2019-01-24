# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_wrong:
    """
    暴力是行不通的，这辈子都行不通的
    Time exceed because endless process of None node.
    """
    def isSymmetricLayer(self,node_list):
        i = 0
        list_len = len(node_list)
        flag = True
        while i <= list_len - 1 - i:
            if node_list[i] is None and node_list[list_len - 1 - i] is None:
                i = i + 1
            elif node_list[i] is None or node_list[list_len - 1 - i] is None:
                return False
            elif node_list[i].val == node_list[list_len - 1 - i].val:
                flag = False
                i = i + 1
            else:
                return False
        if flag:
            return True
        next_layer = []
        for node in node_list:
            if node is None:
                next_layer.append(None)
                next_layer.append(None)
            else:
                next_layer.append(node.left)
                next_layer.append(node.right)
        return self.isSymmetricLayer(next_layer)


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isSymmetricLayer([root.left, root.right])


class Solution_right:
    """
    Discover the base of the problem: the symmetric pair are (left.left, right.right) and (left.right, right.left)
    Problem: why does submissions with same ideas have different running time?
    """
    def isSymmetricPair(self,left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            inner_pair = self.isSymmetricPair(left.left, right.right)
            outer_pair = self.isSymmetricPair(left.right, right.left)
            return inner_pair and outer_pair
        else:
            return False


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isSymmetricPair(root.left, root.right)
