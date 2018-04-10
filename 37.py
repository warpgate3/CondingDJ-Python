


nums_txt = '4 1 4 2 3'
def is_jolly(input_num):
    l = [int(n) for n in input_num.split(' ')]
    l2 = l[1:]
    print(l2)
    for n in range(len(l2) - 1):
        m = abs(l2[n] - l2[n + 1])
        print(m)
        if l2.count(m) == 0:
            return 'Not jolly'
    return 'Jolly'


print(is_jolly(nums_txt))




