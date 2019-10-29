import sys

seq, tag = list(), list()
with open('sequences_training.txt', 'r') as file:
    for line in file:
        words = line.split(',')
        seq.append(words[0] + '\n')
        tag.append(words[1])
    file.close()

with open('seq_clean.txt', 'w') as file:
    for line in seq:
        file.write(line)
    file.close()

with open('tags_clean.txt', 'w') as file:
    for line in tag:
        file.write(line)
    file.close()

j = 0
for i in range(len(tag)):
    if i % 1000 == 0:
        j = j + 1
    with open('tags_clean%s.txt' % j, 'a') as file:
        file.write('>'+tag[i])
        file.write(seq[i])
    file.close()
