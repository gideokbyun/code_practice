def menu_print():
    print("----------------")
    print("1. 2단 구구단 출력")
    print("2. 4단 구구단 출력")
    print("3. 프로그램 종료")
    print("----------------")

flag = True
while flag :
    menu_print();
    
    inputValue = int(input("메뉴를 선택 해주세요"))

    if inputValue == 1:
        for num in range(1, 10):
            print("2 X", num, " = ", 2*num)
    elif inputValue == 2:
        num = 1
        while num <= 9:
            print("4 X", num, " = ", 4*num)
            num = num + 1
    elif inputValue == 3:
        falg = False
    else:
        print("1~3 사이의 값을 입력 해주세요")