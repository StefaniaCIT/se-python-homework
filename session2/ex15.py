"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""
x= input()
v= ['a', 'e', 'i', 'o', 'u']
v = sum(x.count(i) for i in v)
print(v)