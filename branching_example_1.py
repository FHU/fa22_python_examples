# Write a program that gets a user's age from the user
# And prints a different joke for different ages
# under 5: "What's orange and sounds like a parrot?"
# between 5 and 10 (inclusive): "Why can’t a T-rex clap their hands?"
# 11 and 12: "I couldn’t figure out why the baseball kept getting larger. Then it hit me."
# between 13 and 18 (inclusive): "What do you call security guards working outside Samsung shops?"
# over 18: "Have you heard where the word “studying” came from?"

user_age = int(input("What is your age? "))

if user_age <= -1:
    print("We asked your age, not IQ.")
elif user_age <= 4:
    print("What's orange and sounds like a parrot?")
elif user_age <= 10:
    print("Why can’t a T-rex clap their hands?")
elif user_age <= 12:
    print("I couldn’t figure out why the baseball kept getting larger. Then it hit me.")
elif user_age <= 18:
    print("What do you call security guards working outside Samsung shops?")
else:
    print("Have you heard where the word “studying” came from?")