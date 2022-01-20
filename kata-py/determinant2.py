import copy

def determinant(matrix):
    result = 69
    def det1(mat):
        result = mat[0][0]
        return result
    def det2(mat):
        result = (mat[0][0]*mat[1][1])-(mat[0][1]*mat[1][0])
        return result

    def det3(mat):
        minor_list = []
        for counter, number in enumerate(range(0, len(mat))):
            minor = copy.deepcopy(mat)
            del minor[0]
            for row in minor:
                del row[counter]
            minor_list.append(minor)
        minor_det = []
        for minor in minor_list:
            minor_det.append(det2(minor))
        result = 0
        for counter, number in enumerate(minor_det):
            if (counter % 2) == 0:
                result = result + (mat[0][counter]*minor_det[counter])
            else:
                result = result - (mat[0][counter]*minor_det[counter])
        return result

    def det4(mat):
        minor_list = []
        for counter, number in enumerate(range(0, len(mat))):
            minor = copy.deepcopy(mat)
            del minor[0]
            for row in minor:
                del row[counter]
            minor_list.append(minor)
        minor_det = []
        for minor in minor_list:
            minor_det.append(det3(minor))
        result = 0
        for counter, number in enumerate(minor_det):
            if (counter % 2) == 0:
                result = result + (mat[0][counter] * minor_det[counter])
            else:
                result = result - (mat[0][counter] * minor_det[counter])
        return result
    def det5(mat):
        minor_list = []
        for counter, number in enumerate(range(0, len(mat))):
            minor = copy.deepcopy(mat)
            del minor[0]
            for row in minor:
                del row[counter]
            minor_list.append(minor)
        minor_det = []
        for minor in minor_list:
            minor_det.append(det4(minor))
        result = 0
        for counter, number in enumerate(minor_det):
            if (counter % 2) == 0:
                result = result + (mat[0][counter] * minor_det[counter])
            else:
                result = result - (mat[0][counter] * minor_det[counter])
        return result

    if len(matrix) == 1:
        return det1(matrix)
    elif len(matrix) == 2:
        return det2(matrix)
    elif len(matrix) == 3:
        return det3(matrix)
    elif len(matrix) == 4:
        return det4(matrix)
    elif len(matrix) == 5:
        return det5(matrix)



m1 = [[1]]
m2 = [ [1, 3], [2,5]]
m3 = [[2,5,3], [1,-2,-1], [1, 3, 4]]
m4 = [[1, 3, 5, 9], [1, 3, 1, 7], [4, 3, 9, 7], [5, 2, 0, 9]]
m5 = [[1, 3, 4, 2, 5], [3, 2, 3, 2, 3], [4, 2, 6, 7, 2], [5, 2, 3, 4, 1], [2, 3, 5, 7, 2]]# = -20


print(determinant(m5))

### Test ###
# for counter, value in enumerate(m3[0]):
#     print(counter, value)

# for column in range(0, 3):
#     print('*')

# for column in m3:
#     print('*')

# m4 = m3.copy()
# del m4[0]
# print(m4)

# print(3 % 2)
