a = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ",)
a = a.strip(" ").lower().replace("-", " ")

match a:
    case "42":
      print("Yes")
    case "forty two":
      print("Yes")
    case _:
      print("No")
