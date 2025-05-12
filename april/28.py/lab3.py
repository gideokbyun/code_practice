#for 문 사용으로 아래 문자열 내 'h'의 개수를 출력
myString = "hello hundai hoho"
count = 0
for i in myString:
    if i == "h":
        count += 1
    else:
        pass


print("문자열 내 h 갯수: ", count)