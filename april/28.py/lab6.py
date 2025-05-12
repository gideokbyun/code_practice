#1부터 20까지의 정수 중 짝수의 합계 계산
total = 0 
for i in range(1, 21):
    if i % 2 != 0:
        continue
    total += i

print(total)