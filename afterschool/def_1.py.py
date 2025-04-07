#정수 3개 입력 받고 평균 반환



input1 = int(input("첫 번째 정수를 입력하시오:"))
input2 = int(input("두 번째 정수를 입력하시오:"))
input3 = int(input("세세 번째 정수를 입력하시오:"))

def add(input1, input2, input3):
    average = round((input1 + input2 + input3) / 3, 3)
    return average
#return은 반환과 종료 둘 중 하나의 역할을 한다. 

print(add(input1, input2, input3))


