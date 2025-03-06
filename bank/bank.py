a = input("Greeting: ")
a = a.strip()
if a.startswith("Hello"):
    print("$0")
elif a.startswith("How"):
    print("$20")
else:
    print("$100")
