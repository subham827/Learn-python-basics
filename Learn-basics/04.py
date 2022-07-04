#Conditional statements
age = 18
if age < 18:
    print("You are not allowed to vote")
    print(age)
elif age >= 18 and age < 21:
    print("You are allowed to vote but not in the same time")
else:
    print("You are allowed to vote")

print("Only indented statements are executed for conditional statements,this print is not in if or else so this will always be executed irrespective of the age")

num = 7.8
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")