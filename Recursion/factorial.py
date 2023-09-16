def helper(n):
    if n==1 or n==0:
        return 1
    return n * helper(n-1)

print(helper(5))