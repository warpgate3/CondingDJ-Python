'''
OOOOOX

OOOOXX

OOOXXX

OOXXXX

OXXXXX

XXXXXX

'''

'''a = 0b0 | 0b111

print(int(str(bin(a)).replace('0b', '')))

for idx in range(0, 6):
    print(int(str(bin(a)).replace('0b', '')))
    a = a << 1'''


n = input('input number ==>')

a = 0
for idx in range(0, int(n)):
    a = a + 2 ** idx
    f = bin(a)[2:].zfill(int(n))
    print(f.replace('1','X').replace('0','O'))


print(2 ** 256)

115792089237316195423570985008687907853269984665640564039457584007913129639936