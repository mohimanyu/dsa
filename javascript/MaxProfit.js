function maxProfit(prices) {
    let minSoFar = prices[0];
    let res = 0;

    for (let i = 0; i < prices.length; i++) {
        minSoFar = Math.min(minSoFar, prices[i]);

        res = Math.max(res, prices[i] - minSoFar);
    }

    return res;
}

const prices = [7, 10, 1, 3, 6, 9, 2];
console.log(maxProfit(prices)); // Output: 8
