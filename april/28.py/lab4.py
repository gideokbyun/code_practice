#for 문을 사용하여 아래 문자열 내 단어 개수를 출력

myString = "It is a great weather with you"
count = 0

for i in myString:
    if i == " ":     # 공백이 나오면 단어 구분
        count += 1

count += 1   # 마지막 단어 포함

print("문자열 단어 갯수: ", count)