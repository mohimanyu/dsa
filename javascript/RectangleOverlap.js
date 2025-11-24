// Given two rectangles, find if the given two rectangles overlap or not.
// Note that a rectangle can be represented by two coordinates, top left and bottom right. So mainly we are given following four coordinates.
// l1: Top Left coordinate of first rectangle.
// r1: Bottom Right coordinate of first rectangle.
// l2: Top Left coordinate of second rectangle.
// r2: Bottom Right coordinate of second rectangle.

// rectanglesOverlap

// Examples:
// Input: l1 = { 0, 10 }, r1 = { 10, 0 }, l2 = { 5, 5 }, r2 = { 15, 0 }
// Output: Rectangles Overlap

// Input: l1 = { 0, 10 }, r1 = { 10, 0 }, l2 = { -10, 5 }, r2 = { -1, 0 }
// Output: Rectangles Don't Overlap

class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
}

function doOverlap(l1, r1, l2, r2) {
  if (l1.x > r2.x || l2.x > r1.x) return false;

  if (r1.y > l2.y || r2.y > l1.y) return false;

  return true;
}

const l1 = new Point(0, 10);
const r1 = new Point(10, 0);
const l2 = new Point(5, 5);
const r2 = new Point(15, 0);

if (doOverlap(l1, r1, l2, r2)) {
  console.log("Rectangles Overlap");
} else {
  console.log("Rectangles Don't Overlap");
}
