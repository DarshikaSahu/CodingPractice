def reverse(num):
    last_digit = 0

    while num >= 0:
        last_digit = last_digit* 10 + num % 10
        num = num // 10

        #last_digit = last_digit + rem_digit

    return last_digit

print(reverse(1234567890))