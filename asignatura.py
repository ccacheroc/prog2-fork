class Asignatura:
    total_asignaturas = 0  # Contador de instancias

    def __init__(self, nombre, codigo, descripcion):
        self.nombre = nombre
        self.codigo = codigo
        self.descripcion = descripcion
        Asignatura.total_asignaturas += 1  # Aumenta el contador cada vez que se crea un curso