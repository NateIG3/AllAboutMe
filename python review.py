# My program is a grade calculator that takes 4 inputs, one for each quarter grade, and returns your highest, lowest, final, and letter grades. My program can be very useful for those of us that don't want to take all the time adding and dividing and would much prefer a computer to do it for us. 

# FUNCTIONS
# Finds the average by adding all 4 numbers and dividing by 4
def average(a, b, c, d):
    x = a + b + c + d
    return x / 4

# Finds the letter grade by identifying which number range the grade resides in, and prints the corrresponding letter grade
def letter(y):
    if y >= 90:
        print("You have an A")
    elif y >= 80 and y < 90:
        print("You have a B")
    elif y >= 70 and y < 80:
        print("You have a C")
    elif y >= 60 and y < 70:
        print("You have a D")
    elif y >= 0 and y < 60:
        print("You have an E")

# MAIN
# List to hold quarter grades
grades = []

# Uses a for loop to ask for the quarter(1-4) grades
for i in range(1, 5):
    grade = int(input(f"What was your quarter {i} grade? "))
# The while loop runs constantly to make sure the grade isn't above 100
    while grade > 100:
        print("Hmm, something isn't right. Please enter the grade again.")
        grade = int(input(f"What was your quarter {i} grade? "))
# Adds grade values to the list "grades"    
    grades.append(grade)

# Uses the "average" function
y = average(grades[0], grades[1], grades[2], grades[3])
print(" ")
print("Stats:")
# Prints the highest grade
print(f"Your highest grade was {max(grades)}")
# Prints the lowest grade
print(f"Your lowest grade was {min(grades)}")
# Prints the final grade
print("Your final grade is", y)
# Prints the final letter grade
letter(y)
