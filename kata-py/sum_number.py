# def get_sum(a,b):
#     result = 0
#     if a == b:
#         result = a
#     elif a < b:
#         list = range(a, b+1)
#         for number in list:
#             result += number
#     elif a > b:
#         list = range(b, a + 1)
#         for number in list:
#             result += number
#     print(result) #

def get_sum(a,b):
    print(sum(range(min(a,b), max(a,b)+1)))

get_sum(3, 1)

# x = range(3, 6)
# for n in x:
#     print(n)
print(sum(range(2, 3)))


