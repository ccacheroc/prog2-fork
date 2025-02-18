class Estudiante:
    total_estudiantes = 0  # Contador de instancias

    def __init__(self, nombre, edad, cursos_inscritos):
        self.nombre = nombre
        self.edad = edad
        self.cursos_inscritos = cursos_inscritos
        Estudiante.total_estudiantes += 1  # Aumenta el contador cada vez que se crea un estudiante

    def inscribir_curso(self, curso):
        self.cursos_inscritos.append(curso)
        print(f"El estudiante {self.nombre} se ha inscrito en el curso {curso}")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print("Cursos inscritos:")
        for curso in self.cursos_inscritos:
            print(f"- {curso}")
        print()

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nCursos inscritos: {self.cursos_inscritos}"


    def __repr__(self):
        return f'"Estudiante({self.nombre}, {self.edad}, {self.cursos_inscritos})"'

    @classmethod
    def desde_tupla(cls,tupla):
        return cls(*tupla)

    @staticmethod
    def edad_valida(edad):
        return str(edad).isdigit() and int(edad) > 18

if __name__== "__main__":
    e1 = Estudiante("Juan", 20, ["Matemáticas", "Física"])
    print(e1)