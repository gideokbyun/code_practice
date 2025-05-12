input_value = int(input("테이블 개수 입력: "))
input_value2 = int(input("행 수 입력: "))
input_value3 = int(input("열 수 입력: "))

for _ in range(input_value):
    for _ in range(input_value2):
        for _ in range(input_value3):
            print("*", end=" ")
        print()
    print()