correct_id = "admin"
correct_pw = "1234"

attempt = 0

while attempt < 5:
    user_id = input("ID 입력: ")
    user_pw = input("PW 입력: ")
    
    if user_id == correct_id and user_pw == correct_pw:
        print("로그인 성공!")
        break
    
    else:
        attempt += 1
        remaining = 5 - attempt
        
        if attempt >= 5:
            print("lock")
        else:
            print(f"ID 또는 PW가 잘못되었습니다. (남은 시도: {remaining})")