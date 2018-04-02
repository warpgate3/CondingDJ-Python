'''
DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤, 문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고, 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다. (예, 454 => 454, 4546793 => 454*67-9-3) DashInsert 함수를 완성하자. 출처

입력 - 화면에서 숫자로 된 문자열을 입력받는다.
"4546793"
출력 - *, -가 적절히 추가된 문자열을 화면에 출력한다.
"454*67-9-3"

def replace_text(nums):
    print("::::", nums)
    if int(nums) % 2 == 0:
        print('*'.join([x for x in nums]))
    else:
        print('-'.join([x for x in nums]))


'''

import re

test_str = '45467935246134531234'

match = re.compile('[02468]{2,}|[13579]{2,}')

def replace_text(nums):
    n_word = nums.group()
    if int(n_word) % 2 == 0:
        return '*'.join([x for x in n_word])
    else:
        return '-'.join([x for x in n_word])

r = match.sub(replace_text, test_str)
print(r)







