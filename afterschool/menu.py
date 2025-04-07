#키보드로부터 두 개의 정수를 입력 받고 저장 이후 아래 메뉴 출력
input_value1 = int(input("첫 번째 입력 값: \t"))
input_value2 = int(input("두 번째 입력 값: \t"))
# first_number = 첫 번째 수,second_number 두 번째 수 입력받기
#1.더하기
#first_number + second_number
#2.빼기
#first_number - second_number
#3.곱하기
#first_number * second_number
#4.나누기
#first_number / second_number
menu = """----------------------------------
    1.더하기
    2.빼기
    3.곱하기
    4.나누기" \
----------------------------"""
print(menu)
#메뉴 출력 후 다시 키보드로부터 메뉴 선택값을 입력 받고,

#Test1
#print(f"{input_value1} + {input_value2} = {input_value1 + input_value2}")
#if == 1,2,3,4 선택받는다.  
#선택한 연산자에 따라 이전 입력 받은 두 수의 연산값을 출력.
#print(각각의 값)


#메뉴 선택
sel_menu = int(input("메뉴를 선택 하세요!\t"))
result = 0
if sel_menu == 1:
    result = input_value1 + input_value2
elif sel_menu == 2:
    result = input_value1 - input_value2
elif sel_menu == 3:
    result = input_value1 * input_value2
elif sel_menu == 4:
    result = input_value1 / input_value2
else:
    result = "잘못된 입력입니다."
#전체적인 구조를 먼저 구성하고 안을 채워넣는다. 

#결과값 출력
print(result)