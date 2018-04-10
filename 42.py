n = input('Enter the number of bulbs:')
light = False
for i in range(int(n)):
    th = i + 1
    if int(n) % (th) == 0:
        light = not light

if light:
    print('yes')
else:
    print('no')