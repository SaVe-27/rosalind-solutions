name_file = r'rosalind_ini6'

with open(name_file + ".txt", 'r') as in_file:
    buffer = in_file.readline().strip()

words = dict()

for word in buffer.split():
    words[word] = words.get(word, 0) + 1

with open(name_file + ".out", 'w') as out_file:
    for word in words.keys():
        out_file.write(f"{word} {words[word]}\n")