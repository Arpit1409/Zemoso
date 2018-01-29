def gcdIter(a, b):
    ans = min(a, b)
    while a%ans != 0 or b%ans != 0:
        ans -= 1
    return ans