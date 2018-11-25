# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            faster = head.next
            slower = head
            while faster is not slower:
                slower = slower.next
                faster = faster.next.next
            start = head
            meeting = slower.next
            while start is not meeting:
                meeting = meeting.next
                start = start.next
            return start
        except:
            return None
