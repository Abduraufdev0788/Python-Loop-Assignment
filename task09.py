from random import randint
a = randint(1000,9999)
while True:
    text = int(input("Parol kiriting: "))
    if 1000 <= text <= 9999:
        if text > a :
            print("juda katta son ")
        elif text == a :
            print("Tabriklaymiz topdingiz!")
            break
        else:
            print("juda kichik son")
    else:
        print("4 xonali son kiriting")