bar = 3

def test():
    global bar
    bar = 4

test()
print(bar)