x_location = int(input("x좌표를 입력하세요:"))

y_location = int(input("y좌표를 입력하세요:"))

if -1000 <= x_location <= 1000:
    if x_location > 0:
        if y_location > 0:
            print("제 1사분면")
        elif y_location < 0:
            print("제 4사분면")
    elif x_location < 0:
        if y_location > 0:
            print("제 2사분면")
        elif y_location < 0:
            print("제 3사분면")
    else: 
        print("사분면에 해당하지 않습니다.")
else:
    print("범위 안에 값을 입력하세요.")
    