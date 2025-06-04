
bar = [val for val in range(1, 11, 2)]
#list 생성 2가지: [ ] . 함수

foo = list(bar)

pos = bar.copy()

kin = bar[:]


bar[0] = 100

print(foo)
print(pos)
print(kin)
