input_value = int(input("테이블 개수 입력: "))
input_value2 = int(input("행 수 입력: "))
input_value3 = int(input("열 수 입력: "))
menu_selection = int(input("""출력 옵션을 선택하세요: 
1. 1부터 시작하여 열 방향으로 증가
2. 1~100 사이 랜덤 값 출력
옵션 (1 또는 2): """))

import random

if menu_selection == 1:
    count = 1
    for _ in range(input_value):
        print(f"테이블 {input_value}")
        for _ in range(input_value2):
            for _ in range(input_value3):
                print(count,end=" ")
                count += 1
            print()
        print()       

elif menu_selection == 2:
    for _ in range(input_value):
        print(f"테이블 {input_value}")
        for _ in range(input_value2):
            for _ in range(input_value3):
                print(random.randint(1,100),end=" ")
            print()
        print()