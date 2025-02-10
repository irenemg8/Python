class Persona:
    #Si queremos llamar a atributos o a métodos de la clase, usar self.algo
    #Hacemos un atributo privado con un doble subrayado

    def __init__(self, nombre, edad):    #Constructor
        #Públicos
        self.nombre = nombre
        #Privados
        self.__edad = edad


    def mostrar(self):    #En python se necesita SIEMPRE Un self para inicializar la clase
        print("Hola "+ self.nombre)


    def get_edad(self):
        return self.__edad
    

if __name__ == "__main__":   #Esto solo se ejecuta cuando se llama desde main explicitamente
    print("Hola desde la clase persona")