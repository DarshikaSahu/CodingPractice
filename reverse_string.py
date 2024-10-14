def reverse(words:str):
    words = words.split(" ")
    temp =""
    first_char = 0
    last_char = len(words) - 1

    while first_char < last_char:
        temp = words[first_char]
        words[first_char] = words[last_char]
        words[last_char] = temp

        first_char += 1
        last_char -= 1

    return ' '.join(words)

print(reverse("hey darshika"))