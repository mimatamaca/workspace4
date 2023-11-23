print("Programa 1 Beto Lista")
print("Una lista es un tipo de dato que puede modificarse")
print("Ademas de llevar indices [0,1,2...n]")

#declaracion de una lista
miLista=["Cadena de texto",15,2.8,"otro dato",25,25,25]
#imprimir los valores de la lista en ventana
print("Valores de la lista :",miLista)

print("Imprime indice de la lista numero 2: ",miLista[2])
print("Imprime el numero de veces contar:",miLista.count(25))
print("Imprime  numero de indice :  ",miLista.index(2.8))
print("Agrega elemento en la lista ",miLista.append("Elemento"))
print("Nueva lista es: ",miLista)
