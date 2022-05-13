#Ejer nº1
'''lst1 = [1,2,3,4,5]
#lst2=[]
#for n in lst1:
#lst2.append(n)
lst2 = [n for n in lst1]
print(lst2)
'''

#Ejer nº2

'''rng = []
for n in range (1200,2001,130):
    rng.append(n)
#print(rng.__str__)
#print(rng[1])
#print(list(rng))
lst=[]
for x in rng:
    lst.append(x)
print(lst)
rng =range(1200,2001,130) #equivalente a la linea 12, 13 y 14
lst=[x for x in rng] #es esquivalente a las lineas 18, 19 y 20
print(lst) # es equivalente a la linea 21
'''

#Ejer nº3

'''lst1=[44,54,64,74,104]
lst2=[]

for n in lst1:
    lst2.append(n+6)
print(f'Version Larga: Lista 1: {lst1}\n Lista2: {lst2}')

lst1=[44,54,64,74,104]
lst2=[n+6 for n in lst1] # Equivalente a las lineas 30,32 y 33
print(f'Version corta: Lista 1: {lst1}\n Lista2: {lst2}')
'''

#Ejer nº4

'''lst1=[2, 4, 6, 8, 10, 12, 14]
lst2=[]

for n in lst1:
    lst2.append(n**2)
print(lst2)

lst1=[2, 4, 6, 8, 10, 12, 14]
lst2=[n**2 for n in lst1]


print(lst2)
'''

#Ejer nº5
'''
lst1=[2, 4, 6, 8, 10, 12, 14]
lst2=[]

#Version  Larga
for n in lst1:
    if (n**2>50):
        lst2.append(n**2)
print(lst2)

#Version corta
lst1=[2, 4, 6, 8, 10, 12, 14]
lst2=[n**2 for n in lst1 if n**2>50]

print(lst2)
'''

#Ejer nº6
'''
dict={"Susuke Ignis": 985, "Chevrolet park Activ": 1100, "Volkswagen CrossUP": 1245, "Masda CX-3": 1254, "Susuki Vitara": 1245, "Nissan Kicks": 1310, "Mazda CX-5": 1672, "Ford Escape": 1625}
lst=[]

lst = [n.upper() for n in dict if dict[n]<1300]

print(lst)
'''

#Ejer nº7
'''
#Version Larga
lst=["NY", "FL", "CA", "VT"]
dict={}
for n in lst:
    dict.setdefault(n,n)
   #dict[n]=n 
print(dict)
#Version Corta
lst=["NY", "FL", "CA", "VT"]
dict={}
dict={n:n for n in lst}
print (dict)
'''

 #Ejer nº8
'''
rng=range(100,161,10)
dict={}

dict={n:(n/100) for n in rng}


print(dict)
'''

#Ejer nº9
#Version larga
dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2={}
for n in dict1:
    if dict1[n]>2000:
        dict2[n]=dict1[n]

print(dict2)

#Version corta
dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2={}

dict2={n:dict1[n] for n in dict1 if dict1[n]>2000}

print(dict2)