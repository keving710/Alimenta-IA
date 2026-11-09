from src.calidad import resumen, tablero, tasa_lote
from src.produccion import registrar_lote


def _lotes():
    lotes = []
    registrar_lote(lotes, "L-001", "2026-09-01", "Yogur", 1000, 20, 72)
    registrar_lote(lotes, "L-002", "2026-09-02", "Yogur", 1000, 60, 72)
    return lotes


def test_tasa_lote():
    assert tasa_lote(_lotes()[0]) == 2.0


def test_resumen_conteo_y_tasa_global():
    r = resumen(_lotes())
    assert r["total_lotes"] == 2
    assert r["tasa_global"] == 4.0
    assert r["lote_mayor_tasa"] == "L-002"


def test_resumen_vacio():
    assert resumen([])["total_lotes"] == 0


def test_tablero_muestra_conteo_y_tasa():
    texto = tablero(_lotes())
    assert "Lotes registrados:        2" in texto
    assert "4.00%" in texto
