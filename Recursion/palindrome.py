def helper(data, i, n):
    if i >= n:
        return True
    if data[i] != data[n]:
        return False
    return helper(data, i+1, n-1)

def palindrome(data):
    return helper(data, 0, len(data)-1)

print(palindrome('AZAkjngejwng'))