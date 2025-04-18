#점수(정수)를 입력 받아
score = int(input("점수를 입력하시오: "))
#입력 점수가0보다 작으면 
if score < 0:
    print("입력 값 오류")
#입력값이 0 이상일 경우 합격 여부 판단

else:
    if score >= 80:
        print("합격")
    else: 
        print("불합격")
        
    #if elif else
    #점수에 따라 등급 부여
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    else:
        print("D")
        
    #중첩 if: A등급이면서 동시에 95점 이상이면
    #"우수상" 출력
    if score >= 95:
        print("우수상")
    if score == 100:
        print("만점 축하!")
    
    #추가 조건: 점수가 100이면 "만점 축하!" 출력