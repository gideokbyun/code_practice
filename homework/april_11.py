#입력 항목: 최근 6개울 총 구매 금액(정수, 단위 원), 최근 6개월간 총 반품 횟수(정수),
#최근 6개월간총 구매 횟수(정수), 가입 개월 수(정수)
total_purchase = int(input("총 구매 금액:"))
total_return = int(input("총 반품 횟수:"))
total_purchase_num = int(input("총 구매 횟수:"))
member_month = int(input("가입 개월 수:"))

#고객 등급 위험 분류
#위험 고객 조건(하나라도 해당되면 위험 고객객)
# 반품률 >= 50%(반품 횟수/구매횟수 * 100)


if total_purchase_num == 0:
    print("구매 횟수가 0입니다. 반품률을 계산할 수 없습니다.")
    
elif total_return > total_purchase_num:
    print("반품 횟수가 구매 횟수보다 많을 수 없습니다.")
else:
    cancel_per = round((total_return / total_purchase_num) * 100, 1)
    if cancel_per >= 50 or (member_month <= 3 and total_purchase <= 10000) or total_return >= 10:
        print(f"반품률: {cancel_per}%")
        print("결과: 위험 고객")
#가입 개월 수가 3개월 이하이고 구매 금액 10000 이하

#반품 횟수가 10회 이상

#우수 고객 조건(아래 모든 조건만족)

#구매금액 200만원 이상
#반품률 <= 10%
#구매 횟수 >= 30회
#가입 개월 수 >= 12개월
    elif total_purchase >= 2000000 and cancel_per <= 10 and total_purchase_num >= 30 and member_month >= 12:
        print(f"반품률: {cancel_per}%")
        print("결과: 우수 고객")
#나머지는 일반 고객
    else:
        print(f"반품률: {cancel_per}%")
        print("결과: 일반 고객")


#구매 횟수가0인 경우: 반품률 계산불가(오류 메세지 출력 후 종료)
#반품 횟수가 구매 횟수보다 큰 경우:입력 오류(오류 메세지 출력 후 종료)