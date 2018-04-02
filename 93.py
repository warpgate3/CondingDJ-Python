'''
일전에 뭐 게임 회사에서 본 간단한 퀴즈 테스트 입니다.

0~9까지의 문자로 된 숫자를 입력 받았을 때, 이 입력 값이 0~9까지의 숫자가 각각 한 번 씩만 사용된 것인지 확인하는 함수를 구하시오.

sample inputs: 0123456789 01234 01234567890 6789012345 012322456789

sample outputs: true false false true false
'''
import re

n = input("숫자를 입력하세요")

def chk_by_regex(input_num):
    return bool(re.compile('^(?=\d*0)(?=\d*1)(?=\d*2)(?=\d*3)(?=\d*4)(?=\d*5)(?=\d*6)(?=\d*7)(?=\d*8)(?=\d*9)\d{10}$')
                .match(input_num))

print(chk_by_regex(n))

