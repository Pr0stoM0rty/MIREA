q = input()
a = q[:q.find('h') + 1] 
b = q[q.find('h') + 1:q.rfind('h')]
c = q[q.rfind('h'):]
q = a + b.replace('h', 'H') + c
print(q)