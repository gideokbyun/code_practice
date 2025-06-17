#위치 인자 + 기본값이 있는 키워드 인자 혼합
def calc_price(product, price, tax=0.10):
    total = int(price * (1 + tax))
    print(f"{product}의 최종 가격은 {total}원입니다.")

#상품명과 가격을 위치 인자로 받고, 부가세율은 키워드 인자로 받도록 하여 최종 가격 계산 함숮 ㅏㄱ성
calc_price("노트북", 1000000)
calc_price("모니터", 300000, tax=0.05)

#부가세율은 없을 경우 기본 10%, 필요 시 tax = 0.08처럼 옵션 조정 가능.
