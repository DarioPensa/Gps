lista = [1,2,3,4,5,6,7,8]
lista2= [1,2,2,3,4,4,6,7]

s =[ lista[i]==lista[i-1] for i in range(len(lista)) ]
s2=[ lista2[i]==lista2[i-1] for i in range(len(lista2)) ]

if True in s:
    print ' c qualcosa chel va no'
if True in s2:
    print 'el va el va'