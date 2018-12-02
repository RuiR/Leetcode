
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """Iterative solution"""
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


class Solution1(object):
    """Recursive solution"""
    def reverseLink(self, prev, head):
        if not head:
            return prev
        node = head.next
        head.next = prev
        return self.reverseLink(head, node)

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        return self.reverseLink(prev, head)



# N1 = ListNode(1)
# N2 = ListNode(2)
# N3 = ListNode(3)
# N4 = ListNode(4)
# N5 = ListNode(5)
# N1.next = N2
# N2.next = N3
# N3.next = N4
# N4.next = N5
#
# so1 = Solution1().reverseList(N1)