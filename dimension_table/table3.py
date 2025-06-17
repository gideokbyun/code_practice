import random

input_value = int(input("테이블 개수 입력: "))
input_value2 = int(input("행 수 입력: "))
input_value3 = int(input("열 수 입력: "))
menu_selection = int(input("""출력 옵션을 선택하세요: 
1. 1부터 시작하여 열 방향으로 증가
2. 1~100 사이 랜덤 값 출력
옵션 (1 또는 2): """))

if menu_selection == 1:
    count = 1
    for i in range(input_value):
        print("테이블", i + 1)
        
        for _ in range(input_value2):
            for _ in range(input_value3):
                print(count, end=" ")
                count += 1
            print()
        print()

elif menu_selection == 2:
    # 출력할 전체 숫자 개수 계산 (테이블 수 × 행 수 × 열 수)
    total = input_value * input_value2 * input_value3

    # 1부터 100까지의 숫자 중에서 중복 없이 total개만큼 무작위로 뽑기
    nums = random.sample(range(1, 101), total)

    # 숫자 리스트에서 하나씩 꺼내기 위한 인덱스 변수 초기화
    idx = 0

    # 테이블 수만큼 반복 (i는 테이블 번호 역할)
    for i in range(input_value):
        # 테이블 번호 출력 (1부터 시작하도록 i + 1)
        print("테이블", i + 1)

        # 각 테이블 안에서 행 수만큼 반복
        for _ in range(input_value2):
            # 한 행에 대해 열 수만큼 숫자 출력
            for _ in range(input_value3):
                # 현재 인덱스에 해당하는 숫자 출력 (중복 없이), 공백으로 구분
                print(nums[idx], end=" ")
                # 다음 숫자를 위해 인덱스 증가
                idx += 1
            # 한 행이 끝나면 줄 바꿈
            print()
        # 한 테이블이 끝나면 빈 줄 출력 (테이블 구분용)
        print()