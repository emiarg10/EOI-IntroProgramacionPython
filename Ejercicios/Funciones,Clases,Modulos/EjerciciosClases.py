class Persona:
    #Nombres=''
    #Apellidos=''

    def __init__(self,nombres,apellidos):
        self.Nombres = nombres
        self.Apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.Nombres,self.Apellidos)

    def caminar(self):
        print('caminando')


profesor = Persona('Billy','Vanegas')
#profesor.Nombres = 'Emi'  #setter
#profesor.Apellidos = 'Salvachua' #setter

alumno = Persona('Pedro','Sanchez')
#alumno.Nombres = 'Pedro' 
#alumno.Apellidos = 'Sanchez'

administrativo = Persona('Johny','Leon')
#administrativo.Nombres = 'Johny'
#administrativo.Apellidos = 'Leon'

print('El profesor: {} {}'.format(profesor.Nombres,profesor.Apellidos))
print('El alumno: {} {}'.format(alumno.Nombres,alumno.Apellidos))
print('El administrativo: {} {}'.format(administrativo.Nombres,administrativo.Apellidos))

print('El alumno: ', alumno)
profesor.caminar()
