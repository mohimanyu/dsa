// Given the head of a singly linked list, reverse the list, and return the reversed list.

// Example 1:

// Input: head = [1,2,3,4,5]
// Output: [5,4,3,2,1]
// Example 2:

// Input: head = [1,2]
// Output: [2,1]
// Example 3:

// Input: head = []
// Output: []

// Constraints:

// The number of nodes in the list is the range [0, 5000].
// -5000 <= Node.val <= 5000

class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

var reverseList = function (head) {
  let prev = null;
  let curr = head;

  while (curr !== null) {
    let after = curr.next;
    curr.next = prev;
    prev = curr;
    curr = after;
  }

  return prev;
};

let originalList = new ListNode(1);
originalList.next = new ListNode(2);
originalList.next.next = new ListNode(3);
originalList.next.next.next = new ListNode(4);
originalList.next.next.next.next = new ListNode(5);

const reversed = reverseList(originalList);

console.log(reversed.val);
console.log(reversed.next.val);
console.log(reversed.next.next.val);
console.log(reversed.next.next.next.val);
console.log(reversed.next.next.next.next.val);
