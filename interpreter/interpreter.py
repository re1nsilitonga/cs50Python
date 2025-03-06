exp = input("Expression: ")
x, y, z = exp.split(" ")
x = int(x)
z = int(z)

if y == "+":
    print(float(f'{x+z}'))
elif y == "-":
    print(float(f'{x-z}'))
elif y == "*":
    print(float(f'{x*z}'))
else:
    print(float(f'{x/z}'))
