def areal(bredde, gjereLengde): 
    høyde = gjereLengde - bredde
    return bredde * høyde


toatalLengeGjerde = int(input("Hva er lengden på arealet: "))
Resultater = []
usortert = []


for i in range(0, toatalLengeGjerde):
    Resultater.append(areal(i, 100)) 
    # print(f"Arealet ble: {areal(i, toatalLengeGjerde)}, med bredde på {i}, og lengde på {toatalLengeGjerde - i}")




for elemnt in Resultater:
    usortert.append(elemnt) 



Resultater.sort(reverse=True)
stortAreal = Resultater[0]


bredde = usortert.index(Resultater[0])  


hoyde = toatalLengeGjerde - bredde

print(f"Største Areal er: {stortAreal}, med bredde på: {bredde}, og høyde på: {hoyde}")