fr = ["apple", "avocado", "banana", "cantaloupe", "grapefruit", "grapes", "honeydew melon", "kiwifruit", "lemon", "lime", "nectarine", "orange", "peach", "pear", "pineapple", "plums", "strawberries", "sweet cherries", "tangerine", "watermelon"]
cl = [130, 50, 110, 50, 60, 90, 50, 90, 15, 20, 60, 80, 60, 100, 50, 70, 50, 100, 50, 80]
d = dict(zip(fr, cl))

a = input("Item: ")
a = a.lower()
if a in d.keys():
    print(f'Calories: {d[a]}')
else:
    None
