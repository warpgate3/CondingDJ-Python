'''
A사무실에는 특정일자의 출퇴근 시간이 기록된 거대한 로그파일이 있다고 한다.

파일의 형식은 다음과 같다. (한 라인에서 앞부분은 출근시간(HH:MM:SS), 뒷부분은 퇴근시간이다)

09:12:23 11:14:35
10:34:01 13:23:40
10:34:31 11:20:10
특정시간을 입력(예:11:05:20)으로 주었을 때 그 시간에 총 몇 명이 사무실에 있었는지 알려주는 함수를 작성하시오.
'''
import datetime

f = open("c:\\list.txt", 'r')


time_list = [l for l in f.readlines()]

def make_datetime(time_txt):
    return datetime.datetime.combine(datetime.date.today(), datetime.time(int(time_txt[0:2]), int(time_txt[3:5]), int(time_txt[6:8])))

def contain_time(base_time, start_time, end_time):
    if start_time <= base_time and end_time >= base_time:
        return 1
    return 0

count = 0
for t_txt in time_list:
    t_split = t_txt.split(' ')
    count += contain_time(make_datetime("11:05:20"), make_datetime(t_split[0]), make_datetime(t_split[1]))

print(count)




