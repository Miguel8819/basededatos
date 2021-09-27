class Telefono():
    def __init__(self,marca,color,precio):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.encendido=False
        
    def encender(self):
        self.encendido=True
        
    def estado(self):
        if(self.encendido):
            return "El telefono esta encendido"
        else:
            return "El telefono esta en apagado"
        
Telefono1 = Telefono ("Samsung","negro","$25000")
Telefono2 = Telefono ("Nokia","Blanco","$17000")

print ("El telefono es marca",Telefono1.marca,", su color es",Telefono1.color,"y su precio es",Telefono1.precio,"pesos")
print ("El telefono es marca",Telefono2.marca,", su color es",Telefono2.color,"y su precio es",Telefono2.precio,"pesos")

Telefono1.encender()
print (Telefono1.estado())


