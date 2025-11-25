// Given the root of a binary tree, determine if it is a valid binary search tree (BST).

// A valid BST is defined as follows:

// The left subtree of a node contains only nodes with keys strictly less than the node's key.
// The right subtree of a node contains only nodes with keys strictly greater than the node's key.
// Both the left and right subtrees must also be binary search trees.

// Example 1:

// Input: root = [2,1,3]
// Output: true
// Example 2:

// Input: root = [5,1,4,null,null,3,6]
// Output: false
// Explanation: The root node's value is 5 but its right child's value is 4.

// Constraints:

// The number of nodes in the tree is in the range [1, 104].
// -231 <= Node.val <= 231 - 1

class TreeNode {
  constructor(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

var isValidBST = function (root) {
  function validate(node, min, max) {
    if (!node) return true;

    if (node.val <= min && node.val >= max) return false;

    return (
      validate(node.left, min, node.val) && validate(node.right, node.val, max)
    );
  }

  return validate(root, -Infinity, Infinity);
};

let BinarySearchTree = new TreeNode(2);
BinarySearchTree.left = new TreeNode(1);
BinarySearchTree.right = new TreeNode(3);

console.log(isValidBST(BinarySearchTree)); // true

let NotBinarySearchTree = new TreeNode(5);
NotBinarySearchTree.left = new TreeNode(1);
NotBinarySearchTree.right = new TreeNode(4);
NotBinarySearchTree.right.left = new TreeNode(3);
NotBinarySearchTree.right.right = new TreeNode(6);

console.log(isValidBST(NotBinarySearchTree)); // false
