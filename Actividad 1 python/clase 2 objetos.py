class Persona():
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.hablando=False
        
    def hablar(self):
        self.hablando=True
        
    def estado(self):
        if(self.hablando):
            return "Las persona esta hablando"
        else:
            return "Las persona esta en silencio"
        
Persona1 = Persona ("Jose",22,75)
Persona2 = Persona ("Maria",25,60)

print ("Mi nombre es",Persona1.nombre,", tengo",Persona1.edad,"años y peso",Persona1.peso,"kilogramos")
print ("Mi nombre es",Persona2.nombre,", tengo",Persona2.edad,"años y peso",Persona2.peso,"kilogramos")

Persona1.hablar()
print (Persona1.estado())


