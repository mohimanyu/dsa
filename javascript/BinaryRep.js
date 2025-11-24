// Given an integer n, the task is to print the binary representation of the number.

// Note: The given number will be maximum of 32 bits, so append 0's to the left if the result string is smaller than 30 length.

// Examples:

// Input: n = 2
// Output: 00000000000000000000000000000010

// Input: n = 0
// Output: 00000000000000000000000000000000

function getBinaryRep(num) {
  let ans = Array(32).fill("0");

  for (let i = 0; i < 32; i++) {
    if (n % 2 === 1) ans[32 - i] = 1;

    n = Math.floor(n / 2);
  }

  return ans.join("");
}

let n = 20435345;
console.log(getBinaryRep(n));
