name_file = r'rosalind_ini2'

with open(name_file + ".txt", 'r') as in_file:
    with open(name_file + ".out", 'w') as out_file:
        for line in in_file:
            out_file.write(str(sum([pow(element,2) for element in map(int, line.split())])))