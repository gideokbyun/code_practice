#사용자로부터 세 개의 정수를 입력받는다(int 변환)
first_num = int(input("첫 번째 정수를 입력하세요:")) #1
second_num = int(input(" 두 번째 정수를 입력하세요:")) #2
third_num = int(input("세 번째 정수를 입력하세요:")) #3

#입력받은 숫자들의 평균을 구한다(first_num + second_num + third_num / 3).
average = round((first_num + second_num + third_num) / 3, 2)   #출력값이 float, 소수점 조절(round) 2번째 자리까지 반올림림

#결과값 출력.
print(f"평균 : {average}")
