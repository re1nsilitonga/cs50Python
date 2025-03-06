def main():
    plate = input("Plate: ")
    if is_valid(plate) == True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    a = ""
    b = ""
    for i in s:
        if s.isalpha() == False:
            if i.isalpha() ==  True:
                a += i
            elif i.isdigit() == True:
                b += i
        else:
            if(len(s)>=2 and len(s)<=6):
                return True
            else:
                return False
    if(str(s[0:2]).isalpha() and len(s)>=2 and len(s)<=6 and str(s).isalnum() and a+b == s and b[0] != "0" or None):
        return True
    else:
        return False

main()
