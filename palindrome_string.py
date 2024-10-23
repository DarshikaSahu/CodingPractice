def palindrome(string):
    first_node = 0
    last_node = len(string) - 1

    while first_node < last_node:
        if string[first_node] != string[last_node]:
            return False
        first_node += 1
        last_node -= 1
    return True

print(palindrome("madam"))
