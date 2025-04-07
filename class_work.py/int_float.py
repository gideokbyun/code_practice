#정수와 실수 각각 하나씩 입력받아 두 수의 차, 결과값의 자료형 출력

#첫 번째 입력받기, int로 변환,
first_int = int(input("정수를 입력하시오:"))
#두 번째 입력받기, float로 변환,
second_float = float(input("실수를 입력하시오:"))
#두 값의 차이 계산(first_int - second_float)
minus_ans = first_int - second_float
#출력 단계(결과값의 자료형)
print(f"{minus_ans}, {type(minus_ans)}")
"""
False
숫자: 0, 0.0
문자: ""
True
False의 반대 모든 경우"
"""