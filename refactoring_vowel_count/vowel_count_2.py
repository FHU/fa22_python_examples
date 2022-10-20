# Write a program that takes a sentance from the user
# and prints the counts of all the vowels in the sentance.
# as a script with string METHODS
user_input = input("Provide a sentance: ")

count_a = user_input.count('a') + user_input.count('A')
count_e = user_input.lower().count('e')
count_i = user_input.lower().count('i')
count_o = user_input.lower().count('o')
count_u = user_input.lower().count('u')

print(f"{count_a} A's\n"
      f"{count_e} E's\n"
      f"{count_i} I's\n"
      f"{count_o} O's\n"
      f"{count_u} U's")
