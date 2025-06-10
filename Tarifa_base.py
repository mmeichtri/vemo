from collections import defaultdict
from datetime import timedelta
from datetime import datetime

class Tarifa:
    def __init__(self, persona):
        self.persona = persona
        self.extraHoraPico = 1
        self.llamadas = defaultdict(list)

    def registrarLlamada(self, tipo, startDate, endDate, fueHoraPico, costo):
        self.llamadas[self.persona].append({
            'tipo': tipo,
            'inicio': startDate,
            'fin': endDate,
            'duracion_min': self.duracionLlamada(startDate, endDate),
            'hora_pico': fueHoraPico,
            'costo': costo
        })
    
    def validar_fechas(self, startDate, endDate):
        if endDate <= startDate:
           raise ValueError("endDate debe ser posterior a startDate")
    
    def esHoraPico(self, startDate):
        hora = startDate.hour
        return 8 <= hora < 20

    def calcularCosto(self, startDate, endDate):
        self.validar_fechas(startDate, endDate)
        costo = 0
        actual = startDate
        while actual < endDate:
            if self.esHoraPico(actual):
                costo += self.costo + self.extraHoraPico
            else:
                costo += self.costo
            actual += timedelta(minutes=1)
        return costo

    def llamadaTieneHoraPico(self, startDate, endDate):
        actual = startDate
        while actual < endDate:
            if self.esHoraPico(actual):
                return True
            actual += timedelta(minutes=1)
        return False


    def duracionLlamada(self, startDate, endDate):
        diferencia = endDate - startDate
        return int(diferencia.total_seconds() / 60)
    
    def realizarLlamadaNacional(self, startDate, endDate, time):
        from TarifaNacional import TarifaNacional
        llamada = TarifaNacional(self.persona)
        return llamada.realizarLlamadaNacional(startDate, endDate, time)
    
    def realizarLlamadaInternacional(self, startDate, endDate, time):
        from TarifaInternacional import TarifaInternacional
        llamada = TarifaInternacional(self.persona)
        return llamada.realizarLlamadaInternacional(startDate, endDate, time)
    
    def getHistorialLlamadas(self):
        return self.llamadas[self.persona]

    