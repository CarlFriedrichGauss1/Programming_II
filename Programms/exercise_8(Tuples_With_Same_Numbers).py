def function(tuple1, tuple2):
    return len(tuple1) == len(tuple2) and set(tuple1) == set(tuple2) and [item for item in tuple1 if tuple1.count(item) > 1 ] == [item for item in tuple2 if tuple2.count(item) > 1]

print(function((3,1,3,2,3), (3,3,3,2,1)))
