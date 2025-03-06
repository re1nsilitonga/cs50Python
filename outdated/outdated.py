months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        tgl = input("Date: ")
        tgl = tgl.strip()
        if "/" in tgl:
            tgl = tgl.split("/")
            if int(tgl[0]) > 12 or int(tgl[1]) > 31:
                raise ValueError
            print(f'{tgl[2]}-{int(tgl[0]):02}-{int(tgl[1]):02}')
            break
        elif "," in tgl:
            tgl = tgl.split(" ")
            if int(months.index(tgl[0])+1) > 12 or int(tgl[1].strip(",")) > 31:
                raise ValueError
            else:
                print(f'{tgl[2]}-{months.index(tgl[0])+1:02}-{int(tgl[1].strip(",")):02}')
                break
        else:
            raise ValueError
    except ValueError:
        pass
