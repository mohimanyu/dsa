from typing import Optional


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1 or not l2:
            return None

        largerList = l1 if len(l1) > len(l2) else l2

        tempL1 = l1
        tempL2 = l2
        resultList: Optional[ListNode]
        for i in range(len(largerList)):
            carry = 0
            if tempL2:
                resultList.value = tempL1.value + tempL2.value
