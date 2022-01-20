from copy import deepcopy
def wave(word):
    word_list = list(word)
    result = []
    for counter, letter in enumerate(word_list):
        word_capital = deepcopy(word_list)
        if not letter.isspace():
            word_capital[counter] = word_list[counter].upper()
            word_join = ''.join(word_capital)
            result.append(word_join)
    return result

# print(wave('two hands'))
print(wave('a       b'))


### Test ###
# x = 'subject'
# print(x[1].upper())
# print(y)
print('a     b'.islower())