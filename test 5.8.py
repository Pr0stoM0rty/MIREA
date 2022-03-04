q = input()
a = q[:q.find('h')] 
b = q[q.find('h'):q.rfind('h') + 1]
c = q[q.rfind('h') + 1:]
q = a + b[::-1] + c
print(q)