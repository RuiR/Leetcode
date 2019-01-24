# Optimize the House Robber III problem step by step

## Simplify the problem incorrectly in my first try

At first, the constraint of "two directly-linked houses can not be robbed at the same night" lead me to a thought: a node can only be robbed with its "grandchild" node. That has two situations:

1. node, node.left.left, node.left.right, node.right.left, and node.right.right
2. node.left and node.right.

This misunderstanding is partially caused by the example. So I failed in the case [4,1,null,2,null,3] where [4+3] is the largest profit instead of max(4+2, 1+3).

In fact, if the robber robs the root, and doesn't rob the child of root, no matter how he robs the grandchild and grandgrandchild, no police will come. So let me think about it again following the hint of
[fun4LeetCode](https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem):+1:. It also shows the steps to solve and optimize a DP problem.

## Optimal Substructure
