# 86 Partition List

### Problem description
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

**You should preserve the original relative order of the nodes in each of the two partitions.**

### Thought

There are several thoughts about this problem:

1. We need to separate the node to two parts: smaller one and larger one. We can create two node list to store the two parts. And relink all nodes from the smaller one to the larger one. This method is intuitive and could reserve the order, but need extra list to store these nodes.

2. If we don't need to reserve the order, we can just create use two nodes head and tail. If node val is smaller than partition, add it before the head. If not, add it after the tail.

3. If we need to reserve the order without using extra space, use the following solution.

## Solution 1

Too long and ugly. Several mistakes and shortcomings which can be addressed:

1. The first line in the while loop is so important because we need to get the next node first. If not, the head node may change inside the while loop and when we need to get the next node of head, we'll get the wrong node.

2. The flag variable all_before and all_after are set for the situation where all node are smaller or larger than the partition value. In that situation, some head and end node will be None. This can be addressed by initializing the head and end node with ListNode(0). See Solution 2 for details.

3. More concise solution handling the head and end node in Solution 2.

```python3
class Solution:
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
        if not head:
            return None
        before_head = None
        before_end = None
        after_head = None
        after_end = None
        all_after = 1
        all_before = 1
        while head:
            next_node = head.next
            if head.val < x:
                if not before_head and not before_end:
                    before_head = head
                    before_end = head
                    all_after = 0
                else:
                    before_end.next = head
                    before_end = head
            else:
                if not after_head and not after_end:
                    after_head = head
                    after_end = head
                    all_before = 0
                else:
                    after_end.next = head
                    after_end = head
            head = next_node
        if all_after:
            after_end = None
            return after_head
        elif all_before:
            before_end = None
            return before_head
        else:
            before_end.next = after_head
            after_end.next = None
            return before_head
```

### Solution 2

```python3
class Solution:
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
        if not head:
            return None
        before_head = before_end = ListNode(0)
        after_head = after_end = ListNode(0)
        while head:
            if head.val < x:
                before_end.next = head
                before_end = before_end.next
            else:
                after_end.next = head
                after_end = after_end.next
            head = head.next
        before_end.next = after_head.next
        after_end.next = None
        return before_head.next
```
