#가변 개수의 숫자를 매개변수로 받는다
def calculate_average(*args):
    count = len(args)
    plus_sum = sum(args)
    avg = plus_sum / count if count > 0 else 0
    return count, plus_sum, round(avg, 3)
#입력 값의 함수, 개수, 합계, 평균 반환
n, s, avg = calculate_average(70, 80, 90)
#n, s, avg = calculate_average(70, 80, 90)
print(f"입력 개수: {n}")
print(f"총합: {s}")
print(f"평균: {avg}")