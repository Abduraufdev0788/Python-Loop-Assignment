text = input("matn kiritng: ")
unli = "a,e,i,o,u"
count = 0


for i in text.lower() :
    if i in unli:
        count +=1
print(f"Unlilar soni :{count}")
         