#학생 점수 기반(우수합격, 합격, 불합격 판별.)

#국어, 영어, 수학 점수 입력받기
korean = int(input("국어 점수를 입력하세요:"))
english = int(input("영어 점수를 입력하세요:"))
math = int(input("수학 점수를 입력하세요:"))

#각각 점수 출력
print(f"국어 점수: {korean}점\n영어 점수: {english}점\n수학 점수: {math}점")
#평균 계산
average = round((korean + english + math) / 3, 1)
print(f"평균: {average}")
#기준에 따라 학점 판정

#우수 합격: 평균 90점 이상, 각각 80점 이상.
if average >= 90 and korean >= 80 and english >= 80 and math >= 80:
    
    print("우수 합격")
#합격: 평균: 70점 이상, 각각 40점 이상
elif average >= 80 and korean >= 40 and english >= 40 and math >= 40:
    print("합격")
#나머지는 불합격.
else:
    print("불합격")
#and, if, float 계산 시 소수점 표현, 우선순위, 우수 합격 먼저 판정.