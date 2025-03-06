d = {}
while True:
    try:
        item = input().upper()
        d[item] += 1
    except KeyError:
        d[item] = 1
    except EOFError:
        for key in sorted(d):
            print(d[key], key)
        break
