memo = [None] * 100


def fibonacci_top_down(n):
    if memo[n] is not None:
        return memo[n]

    if n == 0 or n == 1:
        return n

    memo[n] = fibonacci_top_down(n - 1) + fibonacci_top_down(n - 2)
    return memo[n]


def fibonacci_bottom_up(n):
    fib_list = [0, 1]

    for i in range(2, n + 1):
        next_fib = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_fib)

    return fib_list[n]


print(fibonacci_top_down(45))
print(fibonacci_bottom_up(35))
