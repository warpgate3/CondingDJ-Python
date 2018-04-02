'''
Example:

codingDojang --> coding_dojang

numGoat30 --> num_goat_3_0

위 보기와 같이 CameleCase를 Pothole_case 로 바꾸는 함수를 만들어요!
'''
import re

def camel_to_snake(input):
    p = re.compile('[A-Z0-9]')
    i_list = []
    for a in p.finditer(input):
        i_list.append(a.span()[0])

    i = 0
    sn_text = ''
    for t in input:
        if i_list.count(i) > 0:
            sn_text = sn_text + '_' + t.lower()
        else:
            sn_text = sn_text + t
        i = i + 1

    return sn_text


print(camel_to_snake("numGoat30"))

