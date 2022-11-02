# 2 => 2
# 4 -> 


def num_ways(steps, length, memo):
    # how many options
    if memo[length] is not None:
        return memo[length]
    total = 0
    for step in steps:
        if length-step:
            result = num_ways(steps, length-step, memo)
            total += result
            memo[length] = result
    return total

steps = [1, 2, 3]
n = 4
memo = [None] * (n+1)
memo[0] = 0
memo[1] = 1
memo[2] = 2
print(num_ways(steps, n, memo))

