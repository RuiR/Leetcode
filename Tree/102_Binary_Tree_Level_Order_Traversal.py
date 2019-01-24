class Solution:
    """
    "if node is not None" is slower than "if node"
    """
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ret_list = []
        cur_node_list = [root]
        while cur_node_list:
            val = []
            next_node_list = []
            for node in cur_node_list:
                # This is not necessary because you already check the node before you put it in the node list
                if node:
                    val.append(node.val)
                    if node.left:
                        next_node_list.append(node.left)
                    if node.right:
                        next_node_list.append(node.right)
            ret_list.append(val)
            cur_node_list = next_node_list
        return ret_list
