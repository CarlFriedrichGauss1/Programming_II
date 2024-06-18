def function(infile , check, outfile):


    try:
        with open(infile, 'r') as read_in , open(outfile, 'a') as write_out:
            for line in read_in:
                chars = list(line.split(""))
                for word in chars:
                    if word in check:
                        write_out.write(check[word])
                    else:
                        write_out.write(word)
        return write_out
    except:
        ValueError("Could not open files")




    
infile = r'C:\Users\billr\OneDrive\Υπολογιστής\Programming_II\infile.txt'
outfile = r'C:\Users\billr\OneDrive\Υπολογιστής\Programming_II\outfile.txt'
check = {'orange': 'or', 'apple': 'ap', 'black': 'bl'}
print(function(infile, check, outfile))