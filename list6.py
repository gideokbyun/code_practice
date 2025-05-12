bar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

del bar[3]
print(bar)

bar.pop()
print(bar)

bar.remove(8)
print(bar)#remove는 value값으로 삭제한다. 

bar.remove(10)