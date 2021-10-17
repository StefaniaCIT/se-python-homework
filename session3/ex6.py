"""
    Ex. 6: Scrieti o functie cu un singur parametru (string) care
    intoarce un string cu toate literele stringului primit +1 (adica urmatoarea
    litera din alfabet)

    Raspuns:
        - func('aabbcc')
            ---> 'bbccdd'
"""
def func(text):
   l= [ord(c) for c in text]
   l2 = [c+1 for c in l]
   return(''.join(chr(c)for c in l2))
print(func('aabbcc'))


