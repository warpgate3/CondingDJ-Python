'''
2진법이란, 어떤 자연수를 0과 1로만 나타내는 것이다.
예를 들어 73은 64(2^6)+8(2^3)+1(2^0)이기 때문에 100 1001으로 표현한다.
어떤 숫자를 입력받았을 때 그 숫자를 2진법으로 출력하는 프로그램을 작성하시오.
'''

#print(bin(73)[2:])
a = []
'''for n in range(1, 100):
    a.append(n)
    if sum(a) > 73:
'''
'''
print(bin(0)[2:])
print(bin(1)[2:])
print(bin(2)[2:])
print(bin(3)[2:])
print(bin(4)[2:])
a = 72
b = []
while a:
    print(a)
    b.append(a%2)
    a = int(a/2)

print(b)
b.reverse()
print(b)


def hex_to_bin(n):
    n2 = int(n / 2)
    hex_to_bin(n2)
'''

list = []
def hex_to_bin(n):
    list.append(str(n % 2))
    if n == 1:
        list.reverse()
        return
    return hex_to_bin(int(n / 2))

hex_to_bin(73)
print(''.join(list))


print(bin(73)[2:])



