try:
  age = int(input("Enter your age:"))
  if age >= 18:
    print("You are eligible to vote...")
  else:
    print("you can't vote...")
except ValueError:
  print("please enter valid integer.")
