#세 개의 숫자를 매개변수로 
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(max_of_three(10, 20, 15))
#가장 큰 수를 그 중에서 반환(return)

#max_of_three
