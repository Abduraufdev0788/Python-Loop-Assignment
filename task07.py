for i in range(1,6):
    son = int(input(f'{i}-elementga qiymat kiriting:'))
    if i==1 :
        max_qiymat = son
    elif son > max_qiymat:
        max_qiymat = son
print(max_qiymat)
