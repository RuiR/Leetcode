"""
Key to solve the problem:
    Find out the root from preorder list, and divide inorder list to left tree list and right tree list
Points to remember:
    1. We can avoid using space by passing index instead of a copy of subset.
"""

class Solution:
    def constructChildTree(self, rootValue, rootValueIndex, treeList):
        node = TreeNode(rootValue)
        rootValueIndexInPreorder = self.preorder.index(rootValue)
        self.preorder.pop(rootValueIndexInPreorder)
        if not treeList:
            return node
        if rootValueIndex > 0:
            leftChildTreeList = treeList[0: rootValueIndex]
            leftTreeRoot = self.preorder[0]
            leftChildRootIndex = leftChildTreeList.index(leftTreeRoot)
            node.left = self.constructChildTree(leftTreeRoot, leftChildRootIndex, leftChildTreeList)
        if rootValueIndex < len(treeList) - 1:
            rightChildTreeList = treeList[rootValueIndex + 1:]
            rightTreeRoot = self.preorder[0]
            rightChildRootIndex = rightChildTreeList.index(rightTreeRoot)
            node.right = self.constructChildTree(rightTreeRoot, rightChildRootIndex, rightChildTreeList)
        return node

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        self.preorder = preorder
        rootValue = self.preorder[0]
        rootIndexWithinInorder = inorder.index(rootValue)
        return self.constructChildTree(rootValue, rootIndexWithinInorder, inorder)

class Solution_Elegant:
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
