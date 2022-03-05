q = [int(i) for i in input().split()]
for i in range(1, len(q), 2):
    q[i - 1], q[i] = q[i], q[i - 1]
print(' '.join([str(i) for i in q]))