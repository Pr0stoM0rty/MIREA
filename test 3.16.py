p = int(input())
x = int(input())
y = int(input())
t = x*100+y
z = t + (t * p / 100)
r = int(z // 100)
k = int(z % 100)
print(r, k)