# Unit 4: Ifs, Elses, and Elifs
# If it is dark, then turn on the light

num = 97
if num <= 100:
	print("Hello")
	print("Beautiful")

print("World")

# == - Determines if two values are equal
# != - Determines if two values are not equal
# > - Determines if one value is greater than the other
# < - Determines if one value is less than the other
# <= - Determines one value is less than or equal to
# >= - Determines if one value is greater than or equal to

# Else with ifs
# If-else statement allows you to execute different
# code if the statement is false

seconds = 100
if seconds > 60:
	print("This is over a minute.")
else:
	print("This is less than a minute")

# If the first condition (seconds > 60) is not met
# the else section will execute

# If-elif statements

seconds = 60
if seconds > 60:
	print("This is over a minute.")
elif seconds == 60:
	print("This is exactly a minute.")
else:
	print("This is less than a minute")

# Logical Operations
# Logical Operations allow you to check multiple conditions
# at once, in the same if statement
# and, or, not

# Quadrant Example (x-y coordinate plane)
# Quadrant 1 should contain (3, 5)

x = 3
y = 5
if x > 0 and y > 0:
	print("This point is in Quadrant 1.")
elif x < 0 and y > 0:
	print("This point is in Quadrant 2.")
elif x < 0 and y < 0:
	print("This point is in Quadrant 3.")
else:
	print("This point is in Quadrant 4.")

# and operators need both parts to be true to execute
# or operators need just one part to be true to execute

status = "Empty"

if status == "Empty" or status == "1/8th":
	print("Fill your gas tank!")
else:
	print("You have enough gas.")

# Nested Ifs
# These are if statements within other if statements

grade = 97
if grade >= 70:
	print("Passing")
	if grade >= 90:
		print("You have an A")
else:
	print("Failing")