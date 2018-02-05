def how_many(aDict):
    ans = 0
    for value in aDict.values():
        ans += len(value)
    return ans