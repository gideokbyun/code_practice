bar = [50, 10, 30, 20, 40]

for index in range(5):
    print(bar[index], end=",\t")

bar[0] = 200
bar[4] = 100

print(bar)