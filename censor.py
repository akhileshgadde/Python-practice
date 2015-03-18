# simple censorship program that replaces the censored 'word' in the string with "****"

def censor(text, word):
    words_list = text.split()
    result = []
    for each in words_list:
        if each == word:
            result.append('*' * len(word))
            print result
        else:
            result.append(each)
            print result
    return " ".join (result)

print censor("this hack is wack hack", "hack")
