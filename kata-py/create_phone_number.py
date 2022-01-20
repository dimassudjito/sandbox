# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
#
# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# def create_phone_number(n):
#     i = 0
#     while i < len(n):
#         n[i] = str(n[i])
#         i += 1
#
#     text = ''.join(n)
#     phone = '(' + text[0:3] + ') ' + text[3:6] + '-' + text[6:11]
#
#     print(phone)

def create_phone_number(n):
    print("({}{}{}) {}{}{}-{}{}{}{}".format(*n))

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8 ,9, 0])

