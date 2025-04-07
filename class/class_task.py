#사용자로부터 메뉴 번호를 입력받아
#해당 도형의 면적을 계산하는 프로그램을 작성한다.
"""
1.원
2.삼각형
3.사각형
"""
#유저 입력 받는다.
user_num = int(input("[도형 면적 계산기]\n메뉴 번호를 입력하세요(1.원, 2.삼각형, 3.사각형):"))


def diverse_num():
    global user_num #전역함수 호출
    if user_num == 1:   #원일 때
        half = int(input("반지름을 입력하세요:"))
        return print(f"원의 면적은 {(half **2) *3.14}입니다.")
    elif user_num == 2:     #삼각형일 때
        height = int(input("높이를 입력하세요:"))
        bottom = int(input("밑변를 입력하세요:"))
        return print(f"삼각형의 면적은 {(height * bottom) / 2}입니다.")
    elif user_num == 3:     #사각형일 때
        width = int(input("가로를 입력하세요:"))
        length = int(input("세로를 입력하세요:"))
        return print(f"사갹형의 면적은 {width * length}입니다.")
    else:
        print("잘못된 접근입니다.")
diverse_num()   #함수 호출


