a, b = [int(s) for s in input().split()]
c = ['I'] * a
for i in range(b):
    d, e = [int(s) for s in input().split()]
    for j in range(d - 1, e):
        c[j] = '.'
print(''.join(c))