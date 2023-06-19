from queue import Queue

class Consulta:
    def __init__(self, nombre, correo, mensaje):
        self.nombre = nombre
        self.correo = correo
        self.mensaje = mensaje

    def __str__(self):
        return f"Consulta{{nombre={self.nombre}, correo={self.correo}, mensaje={self.mensaje}}}"

class GestorConsultas:
    def __init__(self):
        self.cola = Queue()

    def nuevaConsulta(self, c):
        self.cola.put(c)

    def atenderConsulta(self):
        consulta = self.cola.get()
        print(consulta)

    def consultaPendientes(self):
        return self.cola.qsize()

gestor = GestorConsultas()

for i in range(5):
    print("Ingresa tu nombre:")
    nombre = input()
    print("Ingresa tu correo:")
    correo = input()
    print("Ingresa el motivo de tu consulta:")
    consulta = input()
    gestor.nuevaConsulta(Consulta(nombre, correo, consulta))

print("Existen:", gestor.consultaPendientes(), "consultas pendientes")

while gestor.consultaPendientes() > 0:
    print("Si desea atender la consulta, presione 1:")
    bandera = input()
    if bandera == "1":
        gestor.atenderConsulta()
        print("Existen:", gestor.consultaPendientes(), "consultas pendientes")
