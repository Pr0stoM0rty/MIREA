a = 8
x = []
y = []
for i in range(a):
    x1, y1 = [int(s) for s in input().split()]
    x.append(x1)
    y.append(y1)
 
c = True
for i in range(a):
    for j in range(i + 1, a):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            c = False
 
if c:
    print('NO')
else:
    print('YES')