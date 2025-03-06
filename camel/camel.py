c = input("camelCase: ")
print("snake_case: ", end="")
for i in range(len(c)):
    if str(c[i]).islower() == True:
        print(c[i], end="")
    else:
        print("_" + c[i].lower(), end="")
print()
