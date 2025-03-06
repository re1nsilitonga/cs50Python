def add(keys):
    d = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    list_of_values.append(d[keys])

list_of_values = []
while True:
  try:
    keys = input("Item: ")
    keys = keys.title()
    add(keys)
    total = sum(list_of_values)
    print(f'Total: ${total:.2f}')

  except EOFError:
    break

  except (ValueError, KeyError):
    pass

