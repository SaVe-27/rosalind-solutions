name_file = r'rosalind_ini3'

with open(name_file + ".txt", 'r') as in_file:
    buffer = []
    
    for line in in_file:
        buffer.append(line)

with open(name_file + ".out", 'w') as out_file:
    idx = list(map(int, buffer[1].split()))
    
    out_file.write(" ".join([buffer[0][idx[2*i]:idx[2*i+1]+1] for i in range(0, int(len(idx)/2))]))