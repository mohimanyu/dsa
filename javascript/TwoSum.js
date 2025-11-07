function twoSum(arr, target) {
    let set = new Set();

    for (let num of arr) {
        let complement = target - num;

        if (set.has(complement)) return true;

        set.add(num);
    }

    return false;
}

let arr = [10, 15, 3, 7];
let target = 17;

console.log(twoSum(arr, target)); // Output: true
