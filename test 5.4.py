q = input()
word = q[:q.find(' ')]
wordsec = q[q.find(' ') + 1:]
print(wordsec + ' ' + word)