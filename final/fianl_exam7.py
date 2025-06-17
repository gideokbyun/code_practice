#리스트와 타겟 숫자를 매개변수로 받는다
def contains(list, target):
    for num in list:
        if num == target:
            return True
    return False
#타겟 숫자의 리스트 내에 있는지 여부를 반환하는
print(contains([1,2,3,4], 3))
#함수 contains(in 사용 금지)