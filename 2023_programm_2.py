def Python(infile , check, outfile):

    try: 
        read_in = open(infile, 'r')
        read_out = open(outfile, 'a')   
        for i in range(len(read_in.readlines())):
            chars_in_line = read_in.readline(i).split("")
        for i in chars_in_line:
            if check.has_key(i) and check[i] == True:
                read_out.write(i)
            elif check.has_key(i) == False:
                read_out.write(i)
            else:
                pass

        return read_out
    except:
        raise ValueError
        
    

infile = r'C:\Users\billr\OneDrive\Υπολογιστής\Programming_II\infile.txt'
outfile = r'C:\Users\billr\OneDrive\Υπολογιστής\Programming_II\outfile.txt'
check = {'orange': True, 'apple': False, 'black': False}
print(Python(infile, check, outfile))


