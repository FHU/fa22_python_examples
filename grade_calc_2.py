# Grade calculator for quizzes
# Ask the user for 5 grades as percents
# Remove the lowest grade
# Calculate the total percentage and print it out
# Calculate the total points if each is worth 50 points

# NOTE: There is a bug in this code. Find it.
# you don't have to fix it, but you're welcome to try :)

strings_are_sequences = "So are Lists"
grades = [] # What is this???
grades.append(float(input("What was the first quiz %?")))
grades.append(float(input("What was the second quiz %?")))
grades.append(float(input("What was the third quiz %?")))
grades.append(float(input("What was the fourth quiz %?")))
grades.append(float(input("What was the fifth quiz %?")))

grades.sort() # How can you do that?
grades.pop() # What happened on this line?

average_grade = sum(grades) / len(grades)
total_points = int(average_grade * 2)
print(f"The average is {average_grade:.2f}% and it is worth {total_points} points.")