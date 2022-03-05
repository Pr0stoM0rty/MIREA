a = [int(s) for s in input().split()]
q, r = [int(s) for s in input().split()]
 
a.append(0)
for i in range(len(a) - 1, q, -1):
    a[i] = a[i - 1]
a[q] = r
print(' '.join([str(i) for i in a]))