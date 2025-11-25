// Given a binary tree, determine if it is height-balanced.

// Example 1:

// Input: root = [3,9,20,null,null,15,7]
// Output: true
// Example 2:

// Input: root = [1,2,2,3,3,null,null,4,4]
// Output: false
// Example 3:

// Input: root = []
// Output: true

// Constraints:

// The number of nodes in the tree is in the range [0, 5000].
// -104 <= Node.val <= 104

class TreeNode {
  constructor(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

var isBalanced = function (root) {
  function check(node) {
    if (!node) return 0;

    const left = check(node.left);
    if (left === -1) return -1;

    const right = check(node.right);
    if (right === -1) return -1;

    if (Math.abs(left - right) > 1) return -1;

    return Math.max(left, right) + 1;
  }

  return check(root) !== -1;
};

const balancedTree = new TreeNode(1);
balancedTree.left = new TreeNode(2);
balancedTree.right = new TreeNode(3);
balancedTree.left.left = new TreeNode(4);
balancedTree.left.right = new TreeNode(5);

console.log(isBalanced(balancedTree)); // true

const unbalancedTree = new TreeNode(1);
unbalancedTree.left = new TreeNode(2);
unbalancedTree.left.left = new TreeNode(3);
unbalancedTree.left.left.left = new TreeNode(4);

console.log(isBalanced(unbalancedTree)); // false
