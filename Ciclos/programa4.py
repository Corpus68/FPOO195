frase_letra=input("Escribe una frase")
letra_frase=input("Escribe una letra")
contador_deletra=0
for i in frase_letra:
    if i == letra_frase:
        contador_deletra += 1
print(f"El numero de letra es en la frase es: {contador_deletra} ")