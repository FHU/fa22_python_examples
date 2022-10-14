size = int(input("How big is our board? "))

# print top
print('_' * (2 * size + 3))

# print odd line
for line_number in range(size):
    if line_number % 2:
        print('|*' + ' *' * size + '|')
    else:
        print('| ' + '* ' * size + '|')

# print bottom
print('-' * (2 * size + 3))