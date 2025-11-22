from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        tempL1 = l1
        tempL2 = l2

        resultList = ListNode(0)
        temp = resultList
        carry = 0

        while tempL1 or tempL2:
            v1 = tempL1.value if tempL1 else 0
            v2 = tempL2.value if tempL2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10

            temp.next = ListNode(digit)
            temp = temp.next

            if tempL1:
                tempL1 = tempL1.next
            if tempL2:
                tempL2 = tempL2.next

        if carry:
            temp.next = ListNode(carry)

        return resultList.next
