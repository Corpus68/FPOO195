palabra = input("Ingrese una palabra")
if len(palabra)>=2:
    for i in range (len(palabra)):
        print ("Letra", i + 1, ":", palabra[i])
else:
    print("Tiene que tener mas de 2 letras")