// Given a struct array of type Height, find max

// struct Height{
//   int feet;
//   int inches;
// }

class Height {
  constructor(feet, inches) {
    this.feet = feet;
    this.inches = inches;
  }
}

function findMaxHeight(arr) {
  let mx = Number.MIN_VALUE;

  for (let i = 0; i < arr.length; i++) {
    let temp = 12 * arr[i].feet + arr[i].inches;
    mx = Math.max(mx, temp);
  }

  return mx;
}

const arr = [
  new Height(1, 3),
  new Height(10, 5),
  new Height(6, 8),
  new Height(3, 7),
  new Height(5, 9),
];
const res = findMaxHeight(arr);
console.log("max :: " + res);
