from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current_node = result
        memory = 0
        while True:
            if not l1: l1 = ListNode()
            if not l2: l2 = ListNode()
            _sum = l1.val + l2.val + memory
            memory, current_node.val = divmod(_sum, 10)
            if l1.next or l2.next:
                current_node.next = ListNode()
                current_node = current_node.next
                l1, l2 = l1.next, l2.next
            else:
                if memory:
                    current_node.next = ListNode(val=memory)
                break
        return result
