# 다이아몬드 별 출력 
# 높이 기준: 삼각형이 height 줄, 전체는 height * 2 - 1 줄

height = 5

# 윗부분
for num_row in range(1, height + 1):
    for _ in range(height - num_row):  # 왼쪽 공백
        print(" ", end="")
    for _ in range(2 * num_row - 1):   # 별
        print("*", end="")
    print()

# 아랫부분
for num_row in range(height - 1, 0, -1):
    for _ in range(height - num_row):  # 왼쪽 공백
        print(" ", end="")
    for _ in range(2 * num_row - 1):   # 별
        print("*", end="")
    print()
