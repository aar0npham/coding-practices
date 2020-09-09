class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = head = ListNode(None)
        carry = 0
        if not (l1 or l2):
            return l1 or l2
