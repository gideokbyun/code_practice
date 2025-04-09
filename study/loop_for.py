for all in range(2, 9, 2):  # 2, 4, 6, 8단
    for i in range(1, 10, 3):  # 곱하는 수: 1~9, 3개씩 묶기
        for j in range(i, i + 3):
            if j <= 9:
                print(f"{all} x {j} = {all*j}", end="\t")
        print()  # 안쪽 줄 바꿈
    print()  # 단 바뀔 때 빈 줄
