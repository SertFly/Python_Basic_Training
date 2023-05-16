speakers_file = open('speakers.txt', 'r', encoding='utf-8')
sym_count = []
for i_line in speakers_file:
    print(i_line, end='')
    sym_count.append(str(len(i_line)))
print()
sym_count_str = '\n'.join(sym_count)
speakers_file.close()
print(sym_count_str)

counts_file = open('sym_count.txt', 'w')
counts_file.write(sym_count_str)
counts_file.write('\n' + str(50))
counts_file.close()