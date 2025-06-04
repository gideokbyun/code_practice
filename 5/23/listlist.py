#사용자로부터 정수 10개 입력받기
print("정수 10개를 입력하세요.")
numbers = []

for val in range(1, 11):
    user_input = int(input(f"{val}번째 정수: "))
    numbers.append(user_input)
#원본 리스트
print("[원본 리스트]\n",numbers)
#처음 5개 원소
print("1. 처음 5개 원소 : \n",numbers[0:5])
#뒤에서 3개 원소
print("2. 뒤에서 3개 원소: \n",numbers[7:11:1])
#짝수 인덱스 원소만 추출
print("3. 짝수 인덱스 원소: \n",numbers[0:11:2])
#리스트를 거꾸로 뒤집은 결과
print("4. 거꾸로 뒤집은 리스트트: \n",numbers[10:-1:-1])
