total = 0
for i in range(1, 6):
    num = int(input(f"{i}정수를 입력하세요: "))
    total += num
    
average = total / 5

print(total)
print(int(average))