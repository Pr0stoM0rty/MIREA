q = input()
if q.count('f') == 1:
    print(-1)
elif q.count('f') < 1:
    print(-2)
else:
    print(q.find('f', q.find('f') + 1))