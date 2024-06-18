
def function(file , N):
    words = 0
    chars_num = 0

    with open(file, 'r') as read_in:
        for line in read_in:
            line_split = line.split()
            words += len(line_split)
            for j in line_split:
                if len(j) >= N:
                    chars_num += 1

    return words, chars_num

print(function(r'C:\Users\billr\OneDrive\Υπολογιστής\Programming_II\infile.txt' , 9))


