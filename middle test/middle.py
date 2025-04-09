#키보드로부터 정수 5개 입력.
count = 1
total = 0 
while count <= 5:
    count += 1
    user_type = int(input("정수를 입력하시오:"))
    total = total + user_type
    average = total / (count - 1)
    
print(f"합계는 {total}")
print(f"평균은 {average}")