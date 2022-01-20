# - Order word
# - Find if the contain the same words
# - Find if the have the same number for their words

import collections

# def anagrams(word, list):
#     result = []
#     for word_list in list:
#         for letter_list in word_list:
#             for letter in word:
#                 if letter
#     pass

def anagrams(word, record):
    result = []
    word_split = list(word)
    for word_record in record:
        word_record_split = list(word_record)
        if collections.Counter(word_split) == collections.Counter(word_record_split):
            result.append(word_record)
    print(result)

# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])


### Test ###
list1 = ["a", "b", "b"]
list2 = ["b", "b", "a"]
y = 'bird'
# x = collections.Counter(list1) == collections.Counter(list2)
# x = set(list1) ==  set(list2)
# x = collections.Counter(list2)
print(sorted(list1))
print(list(y))
