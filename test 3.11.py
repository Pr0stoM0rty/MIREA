s = int(input())
e = s // 100
s = s // 10 % 10
r = s % 10
print(e + s + r)