frutas =['manzana','banana','cherry','kiwi','mango']
'''nuevalista=[]

for fruta in frutas:
    if 'a' in fruta:
        nuevalista.append(fruta)
print(nuevalista)
'''

nuevalista=[fruta for fruta in frutas if 'a' in fruta]
print(nuevalista)