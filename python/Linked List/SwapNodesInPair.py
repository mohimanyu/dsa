# LL: Swap Nodes in Pairs ( ** Interview Question)
# Write a method called swap_pairs inside the LinkedList class.
# This method should swap every two adjacent nodes in the linked list by adjusting the pointers, not the node values.
# You must modify the list in-place and update the head accordingly.
# If the list has an odd number of nodes, the final node remains in its original position.
# You should use a dummy node to simplify the pointer adjustments.
# For example, if the list is 1 -> 2 -> 3 -> 4, the method should transform it to 2 -> 1 -> 4 -> 3.
# If the list has an odd number of nodes, the last node remains in place (e.g., 1 -> 2 -> 3 becomes 2 -> 1 -> 3).


# Input:
# The method operates on the linked list via self.head, which points to the first node or is None for an empty list.
# Each node has an integer value and a next pointer to the next node or None.

# Output:
# No return value (None); the method modifies the linked list in place.
# The self.head attribute must be updated to point to the head of the modified list after swapping.


# Examples:
# Example 1:
# Input List: 1 -> 2 -> 3 -> 4
# Output List: 2 -> 1 -> 4 -> 3
# Explanation: Swap the first pair (1, 2) to get 2 -> 1 -> 3 -> 4, then swap the second pair (3, 4) to get 2 -> 1 -> 4 -> 3.

# Example 2:
# Input List: 1 -> 2 -> 3
# Output List: 2 -> 1 -> 3
# Explanation: Swap the first pair (1, 2) to get 2 -> 1 -> 3. The last node (3) has no pair, so it stays in place.

# Example 3:
# Input List: 1
# Output List: 1
# Explanation: A single node has no pair to swap, so the list remains unchanged.

# Example 4:
# Input List: [] (empty list)
# Output List: []
# Explanation: An empty list has no nodes to swap, so it remains empty.

# Example 5:
# Input List: 1 -> 2
# Output List: 2 -> 1
# Explanation: Swap the only pair (1, 2) to get 2 -> 1.


# Notes:
# Ensure self.head is correctly updated to point to the new first node after all swaps.
# Handle edge cases like empty lists, single nodes, and lists with odd or even node counts.
# Consider using a dummy node to simplify swapping the head node.
