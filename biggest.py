def biggest(aDict):
    ans = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            ans = key
            biggestValue = len(aDict[key])
    return ans