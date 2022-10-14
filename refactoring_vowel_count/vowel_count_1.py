# Write a program that takes a sentance from the user
# and prints the counts of all the vowels in the sentance.
# as a SCRIPT without the string methods

user_input = input("Provide a sentance: ")

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for char in user_input:
    if char == 'a' or char == 'A':
        count_a += 1
    elif char in 'eE':
        count_e += 1
    elif char in 'iI':
        count_i += 1
    elif char in 'oO':
        count_o += 1
    elif char in 'uU':
        count_u += 1

print(f"{count_a} A's\n"
      f"{count_e} E's\n"
      f"{count_i} I's\n"
      f"{count_o} O's\n"
      f"{count_u} U's")
