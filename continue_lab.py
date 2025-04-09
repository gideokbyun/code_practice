#구구단 중 3의 배수단만을 출력하는 프로그램 continue 사용해서 작성

"""3 x 1 = 3
    6 x 1 = 6
    9 x 1 = 9
"""
#3, 6, 9단을 작성하는 for문
for dan in range(2, 10):         # 2단부터 9단까지
    if dan % 3 != 0:             # 3의 배수가 아니면 건너뜀
        continue
    for i in range(1, 10):       # 곱하는 수: 1 ~ 9
        print(f"{dan} x {i} = {dan*i:<4}", end="\t")
    print()  # 각 단을 한 줄로 출력 후 줄바꿈

#3개씩 구별해서 총 9 X 3의 형식으로 만들어야 한다. 

