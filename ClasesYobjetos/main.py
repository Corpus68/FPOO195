from  Personaje import *
from Armas import *

#Solicitar datos del Spartan
print("====El objeto Spartan contiene=====")
nombreS = input ("Escribe el nombre de tu Spartan ")
especieS = input ("Escribe la especie de tu Spartan ")
alturaS = float(input("Escribe la altura de tu Spartan "))
print("")
#Solicitar el datos del Nemesis
print("=====El objeto Nemesis contiene=====")
nombreN = input ("Escribe el nombre del Nemesis ")
especieN = input ("Escribe la especie del Nemesis ")
alturaN = float(input("Escribe la altura del Nemesis "))
print("")

# creamos el objeto Spartan de la clase del personaje
Spartan = Personaje(especieS,nombreS,alturaS)
Nemesis = Personaje(especieN,nombreN,alturaN)
Arma= Armas ()

#Usamos los atributos Spartan
print (Spartan.nombre)
print (Spartan.especie)
print (Spartan.altura)

#Usamos los metodos del Spartan
Spartan.correr (False)
Spartan.lanzarGranada()
print("")

#Usamos los metodos del Arma
Arma.seleccionarArma(Spartan.nombre)
Arma.recargarArma(50)