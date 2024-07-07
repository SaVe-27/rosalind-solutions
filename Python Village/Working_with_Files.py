name_file = r'rosalind_ini5'

with open(name_file + ".txt", 'r') as in_file:
    with open(name_file + ".out", 'w') as out_file:
        even = False
        for line in in_file:
            if even:
                out_file.write(line)
            
            even = not even
                