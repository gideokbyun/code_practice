#주민번호는 13자리
text = input("문자열을 입력하세요: ")
#사용자로부터 주민번호 입력 받아, 유효성 검사.
list = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

calculate = 0
for character in range(12):
    calculate += int(text[character]) * list[character]
#2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 12자리까지 곱한다.
    
#이 결과를 모두 더한다

#더한 결과를 11로 나눈 나머지를 구한다.
result = calculate % 11

ending = (11 - result) % 10
#결과가 두 자리 숫자라면 1의 자리만 사용한다.
if ending == int(text[12]):
    print("유효한 주민번호입니다.")
else:
    print("유효하지 않은 주민번호입니다.")
#최종결과가 주민번호의 마지막 숫자와 일치하면 유효한 주민번호입니다.