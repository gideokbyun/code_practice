# 사용자에게 높이를 입력 받아 입력받은 높이만큼 삼각형을 출력해라
user_i = int(input("높이를 입력하시오:"))

# 문자열은 곱하기를 지원한다. "*" * 2 = "**"
count = 1

while count <= user_i: 
    print("*" * count)
    count += 1
    
    
    