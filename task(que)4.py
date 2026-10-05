age = int(input("Enter your age: "))

if age < 0:
   print("Invalid age")
elif age >= 18:
   print("you are eligible for voting")
else:
   print("your not eligible for voting")