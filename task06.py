text = input("matn kiriting: ")
a = "..."
b = "."
text = text.replace(a,".")
total = 0
for i in text:
    if b == i:
        total+=1
print(total)
        