'''
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.
두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?

999 * 999
'''

'''
l = []
for n1 in reversed(range(1, 1000)):
    for n2 in reversed(range(1, 1000)):
        v = n1 * n2
        if str(v) == ''.join(reversed(str(v))):
            l.append(int(v))

print(max(l))

s = 'apple'
print(s[::-1])
'''

list = []
for n in range(999 * 999, 100 * 100, -1):
    if str(n) == str(n)[::-1]:
        list.append(n)


for n in list:
    print(n)

#906609


