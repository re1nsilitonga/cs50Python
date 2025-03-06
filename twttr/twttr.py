t = input("Input: ")
print("Output: ", end="")
for ch in t:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        print("", end="")
    else:
        print(ch, end="")
print()
