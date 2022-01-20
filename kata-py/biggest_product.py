def solve(arr):
    max = 0
    arr_counter = 0
    result = []
    for array in arr:
        arr_counter += 1
        num_counter = 0
        for number in array:
            result.append(number * arr[arr_counter][num_counter])
            num_counter += 1

    return result

print(solve([[1, 2], [3, 4]]))