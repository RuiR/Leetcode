class Solution1:
    """
    Problems:
    1. Pass trace as a parameter, need to use trace.copy(), because it's a pointer,
       it will record both left subtree and right subtreeself.
    2. Too slow.
    """
    def findLowestCommonAncestor(self):
        i = 0
        while i < min(len(self.p_trace), len(self.q_trace)):
            if self.p_trace[i] != self.q_trace[i]:
                break
            else:
                i = i + 1
        return self.p_trace[i - 1]

    def findNodeTrace(self, root, p, q, trace):
        if root == p:
            trace.append(root)
            self.p_trace = trace.copy()
            self.flag = self.flag - 1
        if root == q:
            trace.append(root)
            self.q_trace = trace.copy()
            self.flag = self.flag - 1
        if self.flag == 0:
            self.ancestor = self.findLowestCommonAncestor()
            return 0
        else:
            trace.append(root)
            if root.left:
                self.findNodeTrace(root.left, p, q, trace.copy())
            if root.right:
                self.findNodeTrace(root.right, p, q, trace.copy())

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.p_trace = []
        self.q_trace = []
        self.flag = 2
        self.findNodeTrace(root, p, q, [])
        return self.ancestor

        
