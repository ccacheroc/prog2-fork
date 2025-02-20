class Horario:
    total_horarios = 0  # Contador de instancias

    def __init__(self,  dia, hora_inicio, hora_fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        Horario.total_horarios += 1  # Aumenta el contador cada vez que se crea un horario