import math

def functions(list1):
    summary = []
    maximum = []
    index_max = []
    for i in list1:
        max = -math.inf
        sum = 0
        ind_final = 0
        ind_point = 0
        for j in i:
            sum += j
            if j >= max:
                max = j
                ind_final =  ind_point
            ind_point += 1
        summary.append(sum)
        maximum.append(max)
        index_max.append(ind_final)

    return summary , maximum, index_max

print(functions([(1,2,3), (1,4,5), (1,6,3)]))
            


