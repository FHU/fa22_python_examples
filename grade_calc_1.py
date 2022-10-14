# Grade calculator for quizzes
# Ask the user for 5 grades as percents
# Calculate the total percentage and print it out
# Calculate the total points if each is worth 50 points

# NOTE: There is a bug in this code. Find it.
"you don't have to fix it, but you're welcome to try :)"

grades1 = float(input("What was the first quiz %?"))
grades2 = float(input("What was the second quiz %?"))
grades3 = float(input("What was the third quiz %?"))
grades4 = float(input("What was the fourth quiz %?"))
grades5 = float(input("What was the fifth quiz %?"))

average_grade = (grades1 + grades2 + grades3 + grades4 + grades5) / 5
total_points = int(average_grade * 2.5)
print(f"The average is {average_grade:.2f}% and it is worth {total_points} points.")