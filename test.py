# 2 => 2
# 4 -> 


def num_ways(steps, length, memo):
    # how many options
    if memo[length] is not None:
        return memo[length]

    result = num_ways(steps, length-1, memo) + num_ways(steps, length-2, memo)
    memo[length] = result
    return result

steps = [1, 2]
n = 4
memo = [None] * (n+1)
memo[0] = 0
memo[1] = 1
memo[2] = 2
print(num_ways(steps, n, memo))