# Write a program that takes a sentance from the user
# and prints the counts of all the vowels in the sentance.
# with functions

def count_vowels(sentance):
    count_a = sentance.count('a') + sentance('A')
    count_e = sentance.lower().count('e')
    count_i = sentance.lower().count('i')
    count_o = sentance.lower().count('o')
    count_u = sentance.lower().count('u')

    return count_a, count_e, count_i, count_o, count_u

def user_menu():
    user_input = input("Provide a sentance: ")
    count_a, count_e, count_i, count_o, count_u = count_vowels(user_input)
    print(f"{count_a} A's\n"
        f"{count_e} E's\n"
        f"{count_i} I's\n"
        f"{count_o} O's\n"
        f"{count_u} U's")
        
if __name__ == "__main__":
    user_menu()