#상품 가격 입력
price = int(input("상품 가격을 입력하세요:"))

#조건에 따른 할인률 적용
# 10만원 이상 구매 시 -> 10%할인
if price >= 100000:
    percent = 0.1
# 5만원 이상, 10 미만은 5%할인
elif 50000 <=price < 100000:
    percent = 0.05
# 5만원 미만, 할인 없음
else:
    percent = 0
#금액 출력은 정수형으로 변환
final_price = int(price - (price * percent))
discount_percentage = int(percent * 100)
discount_price = int(price * percent)


print(f"할인률: {discount_percentage}%")
print(f"할인 금액: {discount_price}원")
print(f"최종 결제 금액: {final_price}원")
    