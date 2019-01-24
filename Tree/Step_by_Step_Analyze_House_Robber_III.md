# Optimize the House Robber III problem step by step

## Simplify the problem incorrectly in my first try

At first, the constraint of "two directly-linked houses can not be robbed at the same night" lead me to a thought: a node can only be robbed with its "grandchild" node. That has two situations:

1. node, node.left.left, node.left.right, node.right.left, and node.right.right
2. node.left and node.right.

This misunderstanding is partially caused by the example. So I failed in the case [4,1,null,2,null,3] where [4+3] is the largest profit instead of max(4+2, 1+3).

```python
class Solution:

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max_val = 0
        def robMaxMoney(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            cur_val = node.val
            if node.left:
                if node.left.left:
                    cur_val += robMaxMoney(node.left.left)
                if node.left.right:
                    cur_val += robMaxMoney(node.left.right)
            if node.right:
                if node.right.left:
                    cur_val += robMaxMoney(node.right.left)
                if node.right.right:
                    cur_val += robMaxMoney(node.right.right)
            return cur_val
        sib_sum = 0
        if root.left:
            sib_sum += robMaxMoney(root.left)
        if root.right:
            sib_sum += robMaxMoney(root.right)
        root_sum = robMaxMoney(root)
        return max(root_sum, sib_sum)
```

In fact, if the robber robs the root, and doesn't rob the child of root, no matter how he robs the grandchild and grandgrandchild, no police will come. So let me think about it again following the hint of
[fun4LeetCode](https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem):+1:. It also shows the steps to solve and optimize a DP problem.

## Optimal Substructure
The optimal substructure in this problem is "if we want to rob maximum amount of money from current binary tree (rooted at root), we surely hope that we can do the same to its left and right subtrees". This leads to a recursive solution. So we need to think about the two properties of a recursive solution:

1. Termination condition or base condition:

In my first try, there are two termination condition: node is null or node has 0 child. In fact, we can only have **one** termination condition (node is null).

2. Recursive
There are two situations as we stated above, and we only return the maximum of the two situations.

```python
class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        cur_val = root.val
        sib_sum = 0
        if root.left:
            sib_sum += self.rob(root.left)
            if root.left.left:
                cur_val += self.rob(root.left.left)
            if root.left.right:
                cur_val += self.rob(root.left.right)
        if root.right:
            sib_sum += self.rob(root.right)
            if root.right.left:
                cur_val += self.rob(root.right.left)
            if root.right.right:
                cur_val += self.rob(root.right.right)
        return max(cur_val, sib_sum)
```
This method exceed time limit because it has many repeated operations. When we consider one node, we need to calculate the set (node.left.left, node.left.right, node.right.left, and node.right.right, node.left, node.right). When we calculate node.left and node.right, we still need to consider node.left.left, node.left.right..... The overlapping of the subproblems + optimal substructure push us to Dynamic programming.

## Memorize the subproblems.

We could use a hash table (dict in Python) to memorize the solved subproblems. The following code
took 60 ms, faster than 85.47% of Python3 online submissions.

```python
class Solution:
    def robNode(self, root):
        if not root:
            return 0
        if root in self.node_dict:
            return self.node_dict[root]
        cur_val = root.val
        sib_sum = 0
        if root.left:
            sib_sum += self.robNode(root.left)
            if root.left.left:
                cur_val += self.robNode(root.left.left)
            if root.left.right:
                cur_val += self.robNode(root.left.right)
        if root.right:
            sib_sum += self.robNode(root.right)
            if root.right.left:
                cur_val += self.robNode(root.right.left)
            if root.right.right:
                cur_val += self.robNode(root.right.right)
        self.node_dict[root] = max(cur_val, sib_sum)
        return self.node_dict[root]

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.node_dict = {}
        return self.robNode(root)

```
