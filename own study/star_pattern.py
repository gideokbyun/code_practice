#자연수 N을 입력 받아서, 지정된 패턴으로 별(*)출력
N = int(input("N 입력: "))
#첫 번째~N번째 줄 별 개수 1씩 증가
count1 = 0
for i in range(0, N):
    print(i * "*")
    count1 += 1
count2 = N
for i in range(N, 0, -1):
    print(i * "*")
    count2 -= 1
#N번째 줄 이후부터는 별 개수 감소시켜 마지막에는 1개만 출력