def helper(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return (helper(n-1) + helper(n-2))

print(helper(6))


# 0 1 1 2 3 5 8 13 21