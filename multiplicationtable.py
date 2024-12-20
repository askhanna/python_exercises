print('   1  2  3  4  5  6  7  8  9 10')
print('  +----------------------------')
for i in range(1, 11):
    print(i, end='|')
    for j in range(1, 11):
        print('{:3}'.format(i * j), end='')
    print()



