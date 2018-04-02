text = ''
for n in range(1001): text = text + str(n)
for c in range(10): print(str(c), text.count(str(c)))
