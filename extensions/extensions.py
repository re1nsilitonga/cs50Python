a = input("File name: ")
a = a.lower().strip().split(".")

match a[-1]:
    case "gif" | "jpeg" | "png":
        print(f'image/{a[-1]}')
    case "jpg":
        print("image/jpeg")
    case "pdf" | "zip":
        print(f'application/{a[-1]}')
    case "txt":
        print("text/plain")
    case _ :
        print("application/octet-stream ")
