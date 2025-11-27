// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

// Constraints:

// 1 <= strs.length <= 200
// 0 <= strs[i].length <= 200
// strs[i] consists of only lowercase English letters if it is non-empty.

// var longestCommonPrefix = function (strs) {
//   if (strs.length == 1) {
//     return strs[0];
//   } else {
//     min_length = Infinity;
//     for (let i = 0; i < strs.length; i++) {
//       if (strs[i].length < min_length) {
//         min_length = strs[i].length;
//       }
//     }

//     let index = 0;
//     let cp = [];
//     let isMatching = true;

//     while (index <= min_length) {
//       if (isMatching) {
//         for (let i = 0; i < strs.length - 1; i++) {
//           if (strs[i][index] === strs[i + 1][index]) {
//             if (i === strs.length - 2) {
//               cp.push(strs[i][index]);
//             }
//           } else {
//             isMatching = false;
//             break;
//           }
//         }
//       } else break;
//       index += 1;
//     }
//     return cp.join("");
//   }
// };

var longestCommonPrefix = function (strs) {
  class TrieNode {
    constructor() {
      this.children = {};
      this.isEndOfWord = false;
    }
  }

  class Tries {
    constructor() {
      this.root = new TrieNode();
    }

    insert(word) {
      let node = this.root;

      for (let char of word) {
        if (!node.children[char]) {
          node.children[char] = new TrieNode();
        }

        node = node.children[char];
      }

      node.isEndOfWord = true;
    }

    startsWith(word) {
      let node = this.root;

      for (let char in word) {
        if (!node.children[char]) return false;

        node = node.children[char];
      }

      return true;
    }
  }

  const trie = new Tries();
  for (let str of strs) {
    trie.insert(str);
  }

  let prefix = "";
  let node = trie.root;

  while (true) {
    if (Object.keys(node.children).length === 1 && !node.isEndOfWord) {
      const char = Object.keys(node.children)[0];
      prefix += char;
      node = node.children[char];
    } else {
      break;
    }
  }
  return prefix;
};

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
console.log(longestCommonPrefix(["dog", "racecar", "car"]));
