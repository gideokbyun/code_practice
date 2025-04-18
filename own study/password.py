# 사용자로부터 비밀번호를 입력받는다.
password = input("비밀번호를 입력하세요: ")


has_number = False
has_uppercase = False

# 비밀번호 길이 체크
if len(password) >= 8:
    for char in password:
        if char.isdigit():
            has_number = True
        if char.isupper():
            has_uppercase = True

    # 모든 조건 만족 확인
    if has_number and has_uppercase:
        print("비밀번호가 안전합니다.")
    else:
        print("안전하지 않은 비밀번호입니다.")
else:
    print("비밀번호는 8자 이상이어야 합니다.")
