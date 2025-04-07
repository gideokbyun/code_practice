#길이를 입력하세요: 2


#도형을 선택하세요: 1. 사각형, 2. 삼각형

#각각의 면적을 출력한다. 정사각형, 정삼각형이라고 가정
#1,2 이외 값 입력되면 "잘못된 입력입니다."

input_num = int(input("길이를 입력하세요:"))

input_add = int(input("도형을 선택하세요1. 정사각형, 2. 정삼각형:"))

if input_add == 1:
    print(input_num ** 2)
elif input_add == 2:
    print((input_num ** 2) / 2)
else:
    print("잘못된 입력입니다.")