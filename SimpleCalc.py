import math
name = input("Name: ")
print("hello " +name+ "!")
calc()

def calc():
  print("")
  mode = input("what would you like to do? ")
  if mode == "add":
    addition()
  elif mode == "subtract":
    subtract()
  elif mode == "multiply":
    multiply()
  elif mode == "divide":
    divide()
  elif mode == "die":
    die()
  elif mode == "absolute value":
    absolute_value()
  elif mode == "quadratic":
    quadratic()
  elif mode == "hear a story":
    story()
  elif mode == "sin":
    sine()
  elif mode == "cos":
    cosine()
  elif mode == "tan":
    tangent()
  elif mode == "see secret files":
    sec_file()
  elif mode == "exit":
    print("Good Bye")
  else:
    help()
  break
def addition():
  a = float(input("First Number: "))
  b = float(input("Second Number: "))
  c = a+b
  print("The answer is ", c)
  break
def subtract():
  a = float(input("First Number: "))
  b = float(input("Second Number: "))
  c = a-b
  print("The answer is ", c)
  break
def multiply():
  a = float(input("First Number: "))
  b = float(input("Second Number: "))
  c = a*b
  print("The answer is ", c)
  break
def divide():
  a = float(input("Numerator: "))
  b = float(input("Denominator: "))
  if b == 0:
    print("denominator cannot be 0")
  else:
    c = a/b
    print("The answer is ", c)
  break
def absolute_value():
  a = float(input("Number: "))
  if a < 0:
    b = 2*a
    c = a-b
  else:
    c = a
  print("The answer is ", c)
  break
def quadratic():
  print("The quadratic formula is ax^2-bx+c")
  a = float(input("a =  "))
  b = float(input("b =  "))
  c = float(input("c =  "))
  x = 4*a*c
  y = b*b-x
  denom = 2*a
  if y<0:
    print("The first answer is ",-b/denom,"+",math.sqrt(abs(y))/denom,"i")
    print("The second answer is ",-b/denom,"-",math.sqrt(abs(y))/denom,"i")
  else:
    print("The first answer is ",-b/denom,"+",math.sqrt(y)/denom,"i")
    print("The second answer is ",-b/denom,"-",math.sqrt(y)/denom,"i")
  break
def sine():
  a = float(input("Number "))
  print("The answer is ",math.sin(a))
  break
def cosine():
  a = float(input("Number "))
  print("The answer is ",math.cos(a))
  break
def tangent():
  a = float(input("Number "))
  print("The answer is ",math.tan(a))
  break
def story():
  print("There once was a human named "+name+" who asked a calculator to tell it a story")
  print("It failed its math homework...")
  print("The End")
  break
def sec_file():
  print("wow...")
  print("really?")
  break
def die():
  print("hey there champ, keep your chin up")
  break
def help():
  print("")
  print("not a valid command")
  print("valid commands include...")
  print("add")
  print("subtract")
  print("multiply")
  print("divide")
  print("absolute value")
  print("quadratic")
  print("sin")
  print("cos")
  print("tan")
  print("hear a story")
  print("see secret files")
  break
