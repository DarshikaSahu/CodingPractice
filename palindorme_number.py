def palindrome(num):
    rem_digit = num
    last_digit = 0

    while num >= 10:
        last_digit = last_digit + num % 10
        rem_digit= rem_digit // 10
        last_digit = last_digit * 10

    last_digit = last_digit + rem_digit

    return num == last_digit

print(palindrome(121212121))
