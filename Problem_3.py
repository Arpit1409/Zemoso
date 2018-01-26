s = input()
ctr = 0
temp = s[0]
ans = s[0]
for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        temp += s[i + 1]
        if len(temp) > ctr:
            ctr = len(temp)
            ans = temp
    else:
        temp=s[i + 1]
    i += 1
print (ans)