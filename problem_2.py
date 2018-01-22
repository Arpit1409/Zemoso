ctr = 0
for x in range(len(s) - 2):
    if s[x:x+3] == 'bob':
        ctr += 1
print(ctr)