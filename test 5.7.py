q = input()
q = q[:q.find('h')] + q[q.rfind('h') + 1:]
print(q)