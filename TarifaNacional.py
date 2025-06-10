from Tarifa_base import Tarifa

class TarifaNacional(Tarifa):
    costo = 1

    def __init__(self, persona):
        super().__init__(persona)

    def realizarLlamadaNacional(self, startDate, endDate):
        fueHoraPico = self.llamadaTieneHoraPico(startDate, endDate)
        costo = self.calcularCosto(startDate, endDate)
        tipo = "Nacional - Hora Pico" if fueHoraPico else "Nacional - No Pico"
        self.registrarLlamada(tipo, startDate, endDate, fueHoraPico, costo)
        return costo

   