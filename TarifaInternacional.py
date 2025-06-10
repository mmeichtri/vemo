from Tarifa_base import Tarifa
    
class TarifaInternacional(Tarifa):
    costo = 1.5

    def __init__(self, persona):
        super().__init__(persona)

    def realizarLlamadaInternacional(self, startDate, endDate):
        duracion = self.duracionLlamada(startDate, endDate)
        fueHoraPico = self.llamadaTieneHoraPico(startDate, endDate)
        if fueHoraPico:
            costo = self.calcularCosto(startDate, endDate)
            tipo = "Internacional - Hora Pico"
        else:
            costo = duracion * self.costo
            tipo = "Internacional - No Pico"
        self.registrarLlamada(tipo, startDate, endDate, fueHoraPico, costo)
        return costo
