def function(str1, str2):
    common = set(set(str1) & set(str2))
    non_common = set(set('0123456789') - (set(str1) | set(str2)))

    return list(common) , list(non_common)

print(function('a1b2c3' , 'a2f5jh6'))