from datetime import datetime, timedelta
import pytest
from TarifaNacional import TarifaNacional
from TarifaInternacional import TarifaInternacional

def test_llamadaNacionalEnHorarioNoPico():
    llamada = TarifaNacional("Juan")
    inicio = datetime(2025, 6, 10, 9, 0)
    fin = inicio + timedelta(minutes=10)
    costo = llamada.realizarLlamadaNacional(inicio, fin)
    historial = llamada.getHistorialLlamadas()
    assert len(historial) == 1
    assert costo == 20

def test_llamadaInternacionalEnHorarioNoPico():
    llamada = TarifaInternacional("Juan")
    inicio = datetime(2025, 6, 10, 9, 0)
    fin = inicio + timedelta(minutes=10)
    costo = llamada.realizarLlamadaInternacional(inicio, fin)
    historial = llamada.getHistorialLlamadas()

    assert costo == 25
    assert len(historial) == 1

def test_llamadaNacionalEnHoraPico():
    llamada = TarifaNacional("Juan")
    inicio = datetime(2024, 6, 10, 9, 0) 
    fin = inicio + timedelta(minutes=10)
    costo = llamada.realizarLlamadaNacional(inicio, fin)
    historial = llamada.getHistorialLlamadas()

    assert costo == 20
    assert len(historial) == 1

def test_calcularCosto_iniciHoraPico_finHoraNoPico():
    llamada = TarifaNacional("Ana")
    inicio = datetime(2025, 6, 10, 19, 58)
    fin = inicio + timedelta(minutes=10)
    
    costo = llamada.calcularCosto(inicio, fin)
    
    assert costo == 12

def test_fecha_invalida_lanzar_error():
    llamada = TarifaNacional("Juan")
    inicio = datetime(2025, 6, 10, 10, 0)
    fin = datetime(2025, 6, 10, 9, 0) 

    with pytest.raises(ValueError, match="endDate debe ser posterior a startDate"):
        llamada.realizarLlamadaNacional(inicio, fin)