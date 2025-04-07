#상품 가격 입력.
price = int(input("상품 가격을 입력하세요:"))

#조건에 따른 할인률 적용
# 10만원 이상 구매 시 -> 10%할인
if price >= 100000:
    print("할인률: 10%")
    discount_10 = int(price * 0.10)
    print(f"할인 금액: {discount_10}원")
    final_10 = price - discount_10
    print(f"최종 결제 금액: {final_10}원")

    
# 5만원 이상, 10 미만은 5%할인
elif 50000 <=price < 100000:
    print("할인률: 5%")
    discount_5 = int(price * 0.05)
    print(f"할인 금액: {discount_5}원")
    final_5 = price - discount_5
    print(f"최종 결제 금액: {final_5}원")
# 5만원 미만, 할인 없음
else:
    print("할인률: 없음")
    print("할인 금액: 0원")
    print(f"최종 결제 금액: {price}원")
