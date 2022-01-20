# Moving Zeros To The End
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):
    for element in array:
        if element == 0:
            array.remove(0)
            array.append(0)
    return array


print(move_zeros([1, None, 2, 1, 0, 0, 0]))

# Test
num = [1, 2, 2, 3]
# num.remove(2)
# num.remove(2)
# print(num)