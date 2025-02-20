import estudiante
import profesor
import horario
import asignatura
import aula

if __name__ == "__main__":
    e1 = estudiante.Estudiante("Juan", 20, ["Matemáticas", "Física"])
    e2 = estudiante.Estudiante("Ana", 19, ["Química", "Biología"])
    p1 = profesor.Profesor("Carlos", "Matemáticas", ["Matemáticas"])
    p2 = profesor.Profesor("María", "Física", ["Física"])
    h1 = horario.Horario("Lunes", "8:00", "10:00")
    h2 = horario.Horario("Martes", "10:00", "12:00")
    a1 = asignatura.Asignatura("Matemáticas", 'M1', "matematicas 1")
    a2 = asignatura.Asignatura("Física", 'F1', "fisica 1")
    aula1 = aula.Aula("Aula 1", 30, "A1")