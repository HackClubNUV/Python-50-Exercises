def reverse_line(infilename, outfilename):
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for one_line in infile:
            outfile.write(f'{one_line.rstrip()[::-1]}\n')

reverse_line('abc.txt', 'reverse_password.txt')

file1 = open("reverse_password.txt", "r+")

print (file1.read)