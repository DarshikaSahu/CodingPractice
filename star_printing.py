def pattern(num):
    for row in range(0, num):
        for col in range(row):
            print(" ", end=" ")
        
        for col2 in range(num - row):
            print("*  ", end=" ")
        print()
    

pattern(5)