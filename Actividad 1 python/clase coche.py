class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

    def arrancar(self):
        self.enmarcha=True        #métodos-comportamiento   #esto es equivalente decir miCoche.enmarcha=True
            

    def estado(self):
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está detenido"


miCoche=Coche     #instanciar una clase  #Vamos a crear un primer objeto 

print("El largo de mi coche es", miCoche.largoChasis) #utilizo la nomenclatura del punto para acceder
print("El coche tiene", miCoche.ruedas , "ruedas")

miCoche.arrancar(Coche)  #acá lo pusimos en marcha si anulamos esta línea nos va a dar detenido.
print(miCoche.estado(Coche))                               
                        