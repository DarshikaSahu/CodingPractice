def palindrome(words: str):
    word = ""

    for char in words:
        if char.isalnum():
            word += char

    word = word.lower().split()

    first_index = 0
    last_index = len(words) - 1

    while first_index < last_index:
        if words[first_index] == words[last_index]:
            return True
        
        first_index += 1
        last_index -= 1

    return False

print(palindrome("A man, a plan, a canal, Panama"))