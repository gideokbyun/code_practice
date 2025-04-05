try:
    num = int(input("숫자를 입력하시오:"))
    
    if num >= 0:
        
        if num % 2 == 0:
            print("짝수입니다.")
            
        else:
            print("홀수입니다.")
    else:
        print("양수를 입력하시오.")
        
except ValueError:
    print("잘못된 접근입니다. 숫자를 입력하시오.") 