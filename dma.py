#구구단. 2, 4, 6, 8단 출력.

for value in range(2, 9, 2):
    for i in range(1, 10):
        print(f"{value} X {i} = {value*i}", end = "\t")
        if i % 3 == 0:
            print()
    print()
    
        
        
        