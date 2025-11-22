# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]


# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reorderList(self, head: Node) -> None:
    if not head or not head.next:
        return head

    add_list = []
    temp = head
    while temp:
        add_list.append(temp)
        temp = temp.next

    i = 0
    j = len(add_list) - 1
    while i < j:
        add_list[i].next = add_list[j]
        i += 1
        add_list[j].next = add_list[i]
        j -= 1

    add_list[i].next = None
    return head
