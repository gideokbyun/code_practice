#고객의 주문을 받아 음료 가격과 혜택을 계산하는 프로그램

#입력 항목

#입력값은 전부 문자열.
#음료 종류(coffee, latte, juice)
beverage_type = input("음료를 선택하세요 (coffee, latte, juice):")
#크기(small, medium, large)
size_choice = input("크기를 선택하세요(small, medium, large):")
#멤버십 여부(yes, no)
membership = input("멤버십이신가요?(yes/no):")
#가격 coffee: 3000원, latte: 4000원, juice: 3500원
if beverage_type == "coffee":
    price = 3000
elif beverage_type == "latte":
    price = 4000
else:
    price = 3500
#크기 추가 요금 small: 추가 없음, medium: 500원 추가, large: 1000원 추가
if size_choice == "small":
    size = 0
elif size_choice == "medium":
    size = 500
else:
    size = 1000
total_price = price + size
#멤버십 혜택: 총 금액 10% 할인
if membership == "yes":
    discount_price = price * 0.1
else:
    discount_price = 0
final_price = total_price - discount_price
#결과 출력
print(f"기본 가격: {price}원\n크기 추가 요금: {size}원\n할인 적용: -{int(discount_price)}원\n최종 결제 금액: {int(final_price)}원")
#무료 샷 제공
if membership == "yes":
    if beverage_type == "coffee" or beverage_type == "latte":
        if size_choice == "large":
            print("무료 샷이 제공됩니다!")
            
            
            
        
        
#무료 샷 제공 조건: 멤버십 고객 중 coffee, latte 주문, 크기 large인 경우: "무료 샷이 제공됩니다!
# "