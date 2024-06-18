def function(matrix, vector):
    new_list = [[] for _ in range(len(matrix))]
    if len(matrix[0]) == len(vector):
        for i in range(len(matrix)):
            element = 0
            for j in range(len(matrix[i])):
                element += matrix[i][j] * vector[j][0]
            new_list[i].append(element)
    else:
        new_list = []

    return new_list

print(function([[1,11,3] , [1,2,3] , [1,2,2]] , [[1], [2] , [2]]))

    