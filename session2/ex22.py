"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'
"""
a= input()
l1= []
for i in range (len(a)):
    if i % 2 == 0:
        l1.append(a[i].upper())
    elif i % 2 == 1:
        l1.append(a[i].lower()) 
print("".join(l1))