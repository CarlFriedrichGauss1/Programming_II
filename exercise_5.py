def function(list1, list2):
    new_list = []
    i = 0
    j = 0
    while len(new_list) < len(list1) + len(list2):
        if i == len(list1) and  j != len(list2):
            for k in range(j , len(list2)):
                new_list.append(list2[k])
        elif i != len(list1) and j == len(list2):
            for k in range(i , len(list1)):
                new_list.append(list1[k])
        else:
            if list1[i] < list2[j]:
                new_list.append(list1[i])
                i += 1
            elif list1[i] > list2[j]:
                new_list.append(list2[j])
                j += 1
            else:
                new_list.append(list1[i])
                new_list.append(list2[j])
                i += 1
                j += 1

    return new_list

    #ΓΙΑ ΝΑ ΜΗΝ ΕΧΕΙ ΕΠΑΝΑΜΒΑΝΟΜΕΝΑ ΣΤΟΙΧΕΙΑ ΕΠΙΣΤΡΕΦΟΥΜΕ set(new_list)


print(function([1,2,3,12,13,13,13,14,15], [2,3,4,5,6]))
        