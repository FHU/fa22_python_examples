from collections import Counter


def user_menu():
    "I/O with the proram user"
    # get a sentance from user
    user_input = input("Provide the sentance in which we will count vowels.")
    counts = Counter(user_input)
    # print counts
    print(f"{counts['a']} A's\n{counts['e']} E's\n{counts['i']} I's\n{counts['o']}"
        f" O's\n{counts['u']} U's")


if __name__ == "__main__":
    user_menu()