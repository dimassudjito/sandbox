def scramble(s1, s2):
    s1_list = list(s1)
    s2_list = list(s2)
    if all(letter in s1_list for letter in s2_list):
        print('True')
    else:
        print('False')


scramble('rkqodlw', 'world')

### Test ###
# list1 = [1, 1, 2]
# list2 = [1, 2, 3]
# set1 = set(list1)
# set2 = set(list2)
# result = set1.issubset(set2)
# print(result)
test_list = [9, 4, 5, 8, 10]
sub_list = [10, 5, 4]
# if(all(x in test_list for x in sub_list)):
#     print('True')
# else:
#     print('False')

