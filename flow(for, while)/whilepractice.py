#사용자로부터 정수 5개 입력받는다.

#합계 계산: 입력받은 정수의 합계를 계산한다.

#입력받은 정수의 평균을 계산한다.

#계산된 합계와 평균을 출력한다.
count = 0
total = 0  # total 변수 초기화
while count < 5:  # count가 5가 될 때까지 반복
    input_value = int(input("정수를 입력하시오: "))
    count += 1
    total += input_value  # total에 입력 받은 값을 더함

average = total / 5  # 평균 계산
print("합계:", total)
print("평균:", average)
