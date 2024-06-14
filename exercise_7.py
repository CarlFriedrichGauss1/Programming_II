def function(list):
    max_list = 0
    counter = 1
    for i in range(len(list) - 1):
        if list[i] < list[i+1]:
            max_list = counter
        elif list[i] > list[i+1]:
            counter = 1
        else:
            counter += 1
        
    return max_list

print(function([1,2]))
            
            
