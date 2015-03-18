## to reverse a string without using reversed or extended slice functions
def reverse(text):
    result = []
    for ch in range(len(text)-1, -1, -1):
        result.append(text[ch])
    return "".join(result)

reverse("Python!")
