text = input("matnni kiriting: ")
up = "Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M"
total = 0

for i in (text):
    if i in up:
        total +=1
print(total)
    