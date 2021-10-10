"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""
x = input()
v = list ("aeiouy")
c = list ("bcdfghjklmnpqrstvxz")
v = sum(x.count(i) for i in v)
c = sum(x.count(i) for i in c)
print(v)
print(c)