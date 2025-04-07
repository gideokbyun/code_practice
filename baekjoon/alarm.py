
#시간과 분을 입력했을 때, 45분 일찍 설정되도록 만들어야 한다. 

#분이 0보다 작아지면 시간을 1 줄인다. 


hour_set = int(input("시간을 입력하시오:"))
minute_set = int(input("분을 입력하시오:"))

def alarm_project (hour_set, minute_set):
    alter = minute_set - 45
    if alter < 0:
        hour_set - 1

#
