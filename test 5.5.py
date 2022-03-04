q = input()
if q.count('f') == 1:
    print(q.find('f'))
elif q.count('f') >= 2:
    print(q.find('f'), q.rfind('f'))