def primeNumber(num): 
    isPrime = True
    
    if num == 1 or num == 2:
        return num
    
    if num % 2 == 0:
        return False
    
    for index in range(3, num // 2):
        if num % index == 0:
            return False
        index += 2

    return isPrime

print(primeNumber(19))