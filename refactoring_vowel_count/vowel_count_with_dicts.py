
def count_vowels(sentance):
    # count aeiou in string from user
    vowel_counts= {}
    for letter in 'aeiou':
        vowel_counts[letter] = sentance.lower().count(letter)
    return vowel_counts


def user_menu():
    "I/O with the proram user"
    # get a sentance from user
    user_input = input("Provide the sentance in which we will count vowels.")
    counts = count_vowels(user_input)
    # print counts
    print(f"{counts['a']} A's\n{counts['e']} E's\n{counts['i']} I's\n{counts['o']}"
        f" O's\n{counts['u']} U's")


if __name__ == "__main__":
    user_menu()