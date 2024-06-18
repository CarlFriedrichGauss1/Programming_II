def function(str1: str) -> dict:
    list = [*str1]
    new_dict = {}
    for i in range(len(list)):
        new_dict[i+1] = list[i]

    return new_dict

print(function('hello world'))
