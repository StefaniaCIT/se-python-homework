"""
    Veti primi numere intregi de la tastatura pana primiti stringul 'exit'.
    Va trebui sa printati True (boolean) de fiecare data cand elementul
    primit este par, si False (boolean) de fiecare data cand elemtnul primit
    este impar.

    exemplu:
        Veti primi: 1, 3, 4, 5, 5, 'exit'
        Veti printa:
        False
        False
        True
        False
        False
"""
a = ()
l = []
l1 = []
while a != 'exit':
    a = input()
    if a != 'exit':
        if int(a) % 2 == 0:
            l.append('True')
        else:
            l.append('False')
    elif a == 'exit':
        break
print ('\n'.join(l))