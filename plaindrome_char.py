def palindrome(string: str):
    words = ""

    for char in string:
        if char.isalnum():
            words += char

    words = list(words.lower())

    first_char = 0
    last_char = len(words) - 1

    while first_char < last_char:
        if words[first_char] != words[last_char]:
            return False
        
        first_char += 1
        last_char -= 1

    return True

print(palindrome("A man a plan a canal Panama"))
