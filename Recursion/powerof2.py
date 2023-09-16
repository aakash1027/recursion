def helper(n):
    if n == 1:
        return 2
    return 2 * helper(n-1)

print(helper(5))