"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un strign aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""
import string
import random
a = int(input())
l = []
for i in range(a):
    b= random.choice(string.ascii_lowercase)
    l.append(b)
print (''.join(l))
