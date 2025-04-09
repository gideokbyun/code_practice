for i in range(1, 10):  # 곱해지는 수 (1~9)
    for j in range(2, 9, 3):  # 단 (2, 5, 8) - 한 줄에 3단씩
        line = ""
        for k in range(j, min(j + 3, 10)):  # 한 줄에 3단까지만
            line += f"{i} X {k} = {k*i:<4} "
        print(line)
    print()  # 줄바꿈
