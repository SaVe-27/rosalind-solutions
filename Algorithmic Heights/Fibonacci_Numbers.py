name_file = r'rosalind_fibo'

with open(name_file + ".txt", 'r') as in_file:
    buffer = int(in_file.readline()) + 1

fibo = [0, 1]
for i in range(2, buffer):
    fibo.append(fibo[i-1] + fibo[i-2])

with open(name_file + ".out", 'w') as out_file:
    out_file.write(str(fibo[buffer-1]))