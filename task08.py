n = 0
keyWord = "Abu"
while n < 3:
    password = input("parolni kiriting: ")
    if keyWord == password :
        print("siz togri topdingiz dahosiz")
        break
    else:
        print("qayta urinib koring")
        n+=1
else:
    print("bloklandingiz")