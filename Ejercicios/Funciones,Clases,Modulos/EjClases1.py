class vehiculo:
    #metodo privado
    def __privado(self):
        print('Soy privado') # Solo se puede utilizar dentro de la clase
    def metodo_publico(self):
        print('Soy publico')

g1 = vehiculo()
#g1.__privado()
g1._vehiculo__privado()
g1.metodo_publico()
