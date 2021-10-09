"""
    Veti primi un string de la tastatura.
    Va trebui sa printati un tuplu care sa contina toate literele acelui string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: ('c', 'm', 'i')
"""
a= input()
l1= []
for x in a:
    l1.append(x)
print(tuple(l1))
