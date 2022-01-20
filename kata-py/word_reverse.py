def spin_words(sentence):
    words = sentence.split()
    count = 0
    for word in words:
        if len(word) > 4:
            words[count] = word[::-1]
        count += 1
    print(' '.join(words))

spin_words('Welcome')

### Test code

# txt = "welcome to the jungle"
#
# x = txt.split()
#
# print(x)
# x = 'watermelon'
# print(x[::-1])