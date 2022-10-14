# Get the height of a triangle from the user and print it with *.
#
#   *
#  ***
# *****
#*******

triangle_height = int(input("How high would you like your tirangle to be? "))
message = ['This emporor Zerg', 'We need your help', 'To win the fight!!']

# Need a loop, which one (while or for?)
for line_number in range(0,triangle_height):
    spaces = ' ' * (triangle_height - 1 - line_number)
    asterisks = '*' * (line_number * 2 + 1)
    if line_number < len(message):
        print(spaces + asterisks + spaces + message[line_number])
    else:
        print(spaces + asterisks)