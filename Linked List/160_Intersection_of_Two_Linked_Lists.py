# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getLenDiff(self, head):
        len = 0
        while head:
            len = len+1
        return len


    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        headA_copy = headA
        headB_copy = headB
        len_diff = 0
        while headA and headB:
            headA = headA.next
            headB = headB.next
        if headA:
            longListHead = headA_copy
            shortListHead = headB_copy
            len_diff = self.getLenDiff(headA)
        else:
            longListHead = headB_copy
            shortListHead = headA_copy
            len_diff = self.getLenDiff(headB)
        while len_diff:
            longListHead = longListHead.next
            len_diff = len_diff - 1
        while longListHead:
            if longListHead != shortListHead:
                longListHead = longListHead.next
                shortListHead = shortListHead.next
                continue
            else:
                return longListHead
        return None



A1 = ListNode(1)
A2 = ListNode(2)
C1 = ListNode(3)
C2 = ListNode(4)
C3 = ListNode(5)
B1 = ListNode(6)
B2 = ListNode(8)
B3 = ListNode(7)
B4 = ListNode(9)
A1.next = A2
A2.next = C1
C1.next = C2
C2.next = C3
B1.next= B2
B2.next= B3
B3.next = B4
# B4.next = C1

so = Solution()
result = so.getIntersectionNode(A1,B1)
if result:
    print(result.val)
else:
    print("Null")