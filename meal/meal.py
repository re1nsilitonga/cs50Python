def main():
    time = input("What time is it? ")
    newtime = convert(time)
    if newtime < 12:
        print("breakfast time")
    elif newtime >= 12 and newtime < 18:
        print("lunch time")
    elif newtime >= 18:
        print("dinner time")

def convert(time):
    h, m = time.split(":")
    return int(h) + (int(m)/60)


if __name__ == "__main__":
    main()
