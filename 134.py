'''
피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?
'''
from functools import reduce

numbers = [1, 2]
i = 0
while True:
    result = numbers[i] + numbers[i+1]
    if result >= 4000000:
        break
    i = i + 1

    numbers.append(result)

sum_result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, numbers))
print(sum_result)
