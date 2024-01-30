palabra = input ("Ingrese una palabra")
contador_vocales = 0
for letra in palabra: 
    if letra.lower() in "aeiou":
        contador_vocales += 1
print(f"La palabra '{palabra}' tiene {contador_vocales} vocal(es).  ")

