# Areal funskjon, tar inn bredde og gjere lengde og renger ut arealet 
def areal(bredde, gjereLengde): 
    høyde = gjereLengde - bredde
    return bredde * høyde

# Definerer varabler og spør om lengden op gjerdet
toatalLengeGjerde = int(input("Hva er lengden på arealet: "))
Resultater = []
usortert = []

# Går gjennom alle mulige verider på bredde og sender dette inn i areal funskjonen
for i in range(0, toatalLengeGjerde):
    Resultater.append(areal(i, 100)) 
    # print(f"Arealet ble: {areal(i, toatalLengeGjerde)}, med bredde på {i}, og lengde på {toatalLengeGjerde - i}")



# Lagrer en usortert av resultat 
for elemnt in Resultater:
    usortert.append(elemnt) 


# Sorter listen, for å få den største verdien
Resultater.sort(reverse=True)
stortAreal = Resultater[0]

# Finner bredde ved å finne når den høyeste veriden er i den usortere listen. 
bredde = usortert.index(Resultater[0])  

# Regner høyde ved å ta total lengde på gjeret minus bruden
hoyde = toatalLengeGjerde - bredde


# Printe rut til brukeren støre areal og hvilke bredde og lengde det var.
print(f"Største Areal er: {stortAreal}, med bredde på: {bredde}, og høyde på: {hoyde}")