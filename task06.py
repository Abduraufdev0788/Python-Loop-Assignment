text = input("matn kiriting: ")
a = "..."
b = "."
c = "?"
d = "!"
text = text.replace(a,".").replace(c,".").replace(d,".")
total = 0
for i in text:
    if b == i:
        total+=1
print(total)
        