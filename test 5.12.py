q = input()
s = ''
for i in range(len(q)):
    if i % 3 != 0:
        s = s + q[i]
print(s)