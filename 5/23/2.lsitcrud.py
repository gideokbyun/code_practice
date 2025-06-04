#빈 리스트 items를 작성
items = [10, 20, 30]

count = 0
while count < 4:
    
    print("[현재 리스트 내용]")
    for idx, i in enumerate(items):
        print(f"{idx}: {i}")

#사용자에게 다음 중 하나의 작업 선택
    print("""작업을 선택하세요:
1: 요소 추가 (Create)
2: 요소 조회 (Read)
3: 요소 수정 (Update)
4: 요소 삭제 (Delete)
5: 종료 (Exit)
""")
    user_select = int(input("입력: "))
    count += 1
#1. 요소 추가(create) 리스트 끝에 추가
    if user_select == 1:
        user_input = int(input("추가할 값을 입력하세요: "))
        items.append(user_input)
        print("추가 완료.")
#2. 요소 조회(read) 현재 리스트의 모든 요소를 인덱스와 함께 출력한다
    elif user_select == 2:
        for val in items:
            print(val)
#3. 요소 수정(update) 인덱스와 새로운 값을 입력받아 해당 인덱스의 요소를 수정한다.
# 인덱스가 잘못되었을 경우 안내 메시지를 출력한
    elif user_select == 3:
        user_input = int(input("수정할 인덱스를 입력하세요: "))
        changing_input = int(input("새로운 값을 입력하세요: "))
        items[user_input] = changing_input
        print("수정 완료.")    
#4. 요소 삭제(delete) 인덱스를 입력받아 해당 위치의 요소를 삭제한다.
# 인덱스가 잘못되었을 경우 안내 메시지를 출력한다. 
    elif user_select == 4:
        user_input = int(input("삭제할 인덱스를 입력하세요: "))
        del list[user_input]
#5. 종료(exit)
    elif user_select == 5:
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 번호를 입력하세요.")
#사용자는 작업 번호를 계속 입력할 수 있으며, 5번 입력하면 종료한다.
    print(items)