name = input("Name: ")
print("hello " +name+ "!")
mode = input("what would you like to do?: ")
if mode == "add":
  a = float(input("First Number: "))
  b = float(input("Second Number: "))
  c = a+b
  print("The answer is ", c)
elif mode == "subtract":
  a = float(input("First Number: "))
  b = float(input("Second Number: "))
  c = a-b
  print("The answer is ", c)
elif mode == "multiply":
  a = float(input("First Number: "))
  b = float(input("Second Number: "))
  c = a*b
  print("The answer is ", c)
elif mode == "divide":
  a = float(input("Numerator: "))
  b = float(input("Denominator: "))
  if b == 0:
    print("denominator cannot be 0")
  else:
    c = a/b
    print("The answer is ", c)
elif mode == "die":
  print("hey there champ, keep your chin up")
else:
  print("")
  print("not a valid command")
  print("valid commands include...")
  print("add")
  print("subtract")
  print("multiply")
  print("divide")
