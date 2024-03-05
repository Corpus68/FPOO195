class Personaje:
    
    
    #atributo de personaje.
    #Declaramos el consturctor para crear los objetos
    def __init__(self,esp,nom,alt):
        self.__especie = esp 
        self.__nombre = nom
        self.__altura = alt
        
    def getNombre(self):
        return self.__nombre
    def getEspecie(self):
        return self.__especie
    def getAltura(self):
        return self.__Altura
    
    def setNombre(self,nombre):
        self.__nombre = nombre
        
    def setAltura(self,altura):
        self.__altura = altura
        
    def setAltura(self,altura):
        self.__altura = altura
    
    #metodos del personaje
    def correr (self, estado):
        if(estado):
            print("el personaje "+self.get__nombre() +" esta corriendo")
        else: 
            print ("El personaje "+self.get__nombre() +" esta muerto")
    def lanzarGranada (self):
        print(self.get__nombre + " Pego una granada")
    
        
    
        
  