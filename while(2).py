#입력값이 양수가 아닐 경우, 에러 메시지 출력 후 재입력
#양수를 입력 받을 때까지 
isValid = False
while not isValid:
    input_value = int(input("정수 입력: "))
    
    
    if input_value > 0:
        isValid = True
    else:
        print("양의 정수를 입력하세요")
    
    

#조건식이 거짓인 경우