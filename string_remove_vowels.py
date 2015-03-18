# python program to remove the vowels from the given string and print the result

def anti_vowel(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for item in text:
            if item.lower() not in vowels:
                result.append(item)
    return "".join(result)
print anti_vowel("Hey! How are you!!")
