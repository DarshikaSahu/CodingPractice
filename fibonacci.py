def fib(num):
    num0 = 0
    num1 = 1

    for index in range(1, num+1):
        print(num0, end=" ")
        num0 = num0 + num1
        temp = num0
        num0 = num1
        num1 = temp
    

fib(5)