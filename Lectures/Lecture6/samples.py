# variable assignment
x = 0
s = ""

# input
n = int(input("Insert the number of steps\n"))

# loops
while x < n:
  s = ""
  # conditionals and expressions
  if x % 4 == 0:
    s = s + "/"
  elif x % 4 == 1:
    s = s + "-"
  elif x % 4 == 2:
    s = s + "\\"
  else:
    s = s + "|"
  x = x + 1
# output
print(s)

# various expressions and operator precedence
print(True and True)
print(True and False)
print(not True and False)
print(not (True and False))
print(True or True)
print(True or False)
print(3 + 2 * 5)
print(5 // 2)
print(5 / 2)

# simple conditionals
n = int(input("insert the first operand\n"))
op = input("insert the operation (+,-,*,/)\n")
m = int(input("insert the second operand\n"))
if op == "+":
  res = n + m
elif op == "-":
  res = n - m
elif op == "*":
  res = n * m
else:
  res = n // m
print(f"{n}{op}{m} -> {res}")

# repeating calculator
quit = False
while not quit:
    op = input("insert the operation (+,-,*,/,neg,quit)\n")
    if op == "+":
        n = int(input("insert the first operand\n"))
        m = int(input("insert the second operand\n"))
        res = n + m
        print(str(n) + op + str(m) + " -> " + str(res))
    elif op == "-":
        n = int(input("insert the first operand\n"))
        m = int(input("insert the second operand\n"))
        res = n - m
        print(str(n) + op + str(m) + " -> " + str(res))
    elif op == "*":
        n = int(input("insert the first operand\n"))
        m = int(input("insert the second operand\n"))
        res = n * m
        print(str(n) + op + str(m) + " -> " + str(res))
    elif op == "/":
        n = int(input("insert the first operand\n"))
        m = int(input("insert the second operand\n"))
        res = n // m
        print(str(n) + op + str(m) + " -> " + str(res))
    elif op == "neg":
        n = int(input("insert the only operand\n"))
        res = -n
        print("neg(" + str(n) + ") -> " + str(res))
    elif op == "quit":
        quit = True
        print("Quitting...")
    else:
        print("Operation " + str(op) + " is not recognized.")

n = int(input("insert the number to divide\n"))
b = int(input("insert the divisor\n"))
i = 0
m = n
while m >= b:
  m = m // b
  i = i + 1
print(f"log_{b}({n}) = {i}")

b = int(input("insert the base\n"))
n = int(input("insert the exponent\n"))
i = 0
m = 1
while i < n:
  m = m * b
  i = i + 1
print(f"{b}^{n} = {m}")

