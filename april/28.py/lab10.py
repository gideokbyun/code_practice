#컴퓨터가 1부터 100 사이의 숫자를 랜덤하게 선택
import random

number = random.randint(1, 100)
count = 10

while count > 0:
    input_num = int(input("1~100까지의 숫자를 입력하세요 (0 입력 시 종료): "))

    if input_num == 0:
        print("게임을 종료합니다.")
        break

    if input_num == number:
        print("정답입니다!")
        break

    elif input_num < number:
        print("더 큰 숫자입니다.")
    
    elif input_num > number:
        print("더 작은 숫자입니다.")

    count -= 1  

    if count == 0:
        print(f"모든 기회를 사용하였습니다. 정답은 [{number}]입니다.")

#10번의 기회가 주어짐

#더 큰 숫자입니다, 더 작은 숫자입니다.

#정답입니다. 이후 종료

#10번 시도 끝까지 정답 못 맞추면, 

#"모든 기회를 사용하였습니다. 정답은 [숫자]입니다."  출력

#사용자가 0을 입력하면 언제든지 게임 종료