while True:
    input_value = int(input("정수 입력: " ))
    
    if input_value > 0:
        break
    
    print("양의 정수를 입력하세요.")
    
print("bar") 

#break를 실행하면 첫 번째 만나는 반복문까지 올라간다. 그리고 이 반복문을 탈출한다. 

#위 코드 break에서 while True로 올라가고, print("bar")을 다음에 실행한다. 

#break를 쓰는 이유는 특정 조건에서 반복문을 멈추고 싶을 때. 