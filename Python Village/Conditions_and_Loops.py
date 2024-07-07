name_file = r'rosalind_ini4'

with open(name_file + ".txt", 'r') as in_file:
    with open(name_file + ".out", 'w') as out_file:
        for line in in_file:
            buffer = list(map(int, line.split()))
            out_file.write(str(sum([element for element in range(buffer[0], buffer[1]+1) if element%2 == 1])))