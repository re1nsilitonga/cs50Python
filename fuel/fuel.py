def main():

    a, b = input("Fraction: ").split("/")
    a = int(a)
    b = int(b)

    fuel_left = (a / b) * 100
    fuel_left = round(fuel_left)

    if fuel_left > 100:
      main()

    if fuel_left >= 99 and fuel_left <= 100:
      print("F")

    elif fuel_left <= 2:
      print("E")

    else:
      fuel_left = str(fuel_left)
      fuel_left = fuel_left.strip(".0")
      print(f"{fuel_left}%")

while True:
  try:
    main()
    break

  except (ValueError, ZeroDivisionError):
    pass
