
#숫자 맞추기 게임
import random

number = random.randint(1, 100)
#while, break.
while True:
    input_num = int(input("1~100까지의 숫자를 입력하시요: "))
#사용자가 숫자 맞추면 종료, 그전까지는 반복
    if input_num == number:
        print("정답입니다.")
        break
    elif input_num < number:
        print("더 큰 숫자입니다.")
    elif input_num > number:
        print("더 작은 숫자입니다.")
#정답 숫자를 랜덤 함수를 이용해서 1~100 정수 선택

