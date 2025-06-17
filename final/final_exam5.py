#주어진 수가 짝수인지 홀수인지 판별하는 함수 
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
#is_even

#4,5 를 판별하도록.
print(is_even(4))
print(is_even(5))