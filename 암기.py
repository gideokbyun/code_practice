row = 3
col = 3
for num_row in range(1, row + 1):
    for _ in range(row - num_row):
        print(" ", end="")
    for _ in range(num_row):
        print("*", end="")
        
    print()