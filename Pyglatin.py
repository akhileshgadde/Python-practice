pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    word = original.lower()
    first = word[0]
    if first=="a" or first =="e" or first=="i" or first=="o" or first=="u":
        print "Translation of a string beginning with vowel"
        new_word = word+pyg
        print new_word
    else:
        print "Translation of a string beginning with consonant"
        new_word = word[1:len(word)] + first + pyg
        print new_word
else:
    print "Empty or Invalid string: %s" % (original)

