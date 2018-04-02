print("digital clock")
'''
디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 일까요?

디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됩니다.
00:00 (60초간 표시됨)
00:01 
00:02 
...
23:59
'''

hour_list = range(0, 24)
sec_list = range(0, 60)
total_second = 0
for t in hour_list:
    hour_text = "{:02d}".format(t)
    for s in sec_list:
        second_text = "{:02d}".format(s)
        merge_text = hour_text + second_text
        if str(3) in merge_text:
            total_second += 60


print(total_second)



