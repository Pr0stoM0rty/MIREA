a = [int(i) for i in input().split()]
s = int(input())
m = 0
while m < len(a) and a[m] >= s:
    m += 1
print(m + 1)