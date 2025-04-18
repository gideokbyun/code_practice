#사용자 초기 정보 입력

#초기 자본금
start_money = int(input("초기 자본금: "))
#주식의 구매 가격
buy_stock_price = int(input("주식의 구매 가격: "))
#구매할 주식 수
buy_stock_num = int(input("구매할 주식의 수: "))
#판매할 때의 주식 가격
sell_stock_price = int(input("판매할 때의 주식 가격: "))
#계산 해야 하는 것들

#주식 구매 비용 계산
spend_money = buy_stock_price * buy_stock_num
#남은 자본금(구매 이후)
after_budget = start_money - spend_money
#주식 판매 시 예상 이익 또는 손실
loss_or_earn = (sell_stock_price * buy_stock_num) - spend_money
#결과 출력: 남은 자본금과 이익, 손실 출력

if loss_or_earn > 0:
    print(f"구매 후 남은 자본금: {after_budget}\n예상되는 이익입니다.")
else:
    print(f"구매 후 남은 자본금: {after_budget}\n예상되는 손실입니다.")