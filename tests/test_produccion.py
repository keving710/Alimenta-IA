import pytest

from src.produccion import filtrar_por_producto, registrar_lote, validar_lote


def test_tasa_caso_normal():
    assert validar_lote(200, 6) == 3.0


def test_tasa_sin_defectos():
    assert validar_lote(500, 0) == 0.0


def test_cero_producidas_rechazado():
    with pytest.raises(ValueError):
        validar_lote(0, 0)


def test_negativos_rechazados():
    with pytest.raises(ValueError):
        validar_lote(-10, 0)
    with pytest.raises(ValueError):
        validar_lote(100, -1)


def test_defectuosas_mayores_que_producidas():
    with pytest.raises(ValueError):
        validar_lote(100, 101)


def test_registrar_lote_valido():
    lotes = []
    lote = registrar_lote(lotes, "L-001", "2026-09-01", "Yogur", 1000, 30, 72.5)
    assert lotes == [lote]
    assert lote["temperatura"] == 72.5


def test_codigo_duplicado_rechazado():
    lotes = []
    registrar_lote(lotes, "L-001", "2026-09-01", "Yogur", 1000, 30, 72.5)
    with pytest.raises(ValueError):
        registrar_lote(lotes, "L-001", "2026-09-02", "Yogur", 900, 10, 71)


def test_fecha_invalida_rechazada():
    with pytest.raises(ValueError):
        registrar_lote([], "L-002", "01/09/2026", "Yogur", 1000, 30, 72)


def test_filtrar_por_producto():
    lotes = []
    registrar_lote(lotes, "L-001", "2026-09-01", "Yogur", 1000, 30, 72)
    registrar_lote(lotes, "L-002", "2026-09-02", "Galletas", 800, 20, 70)
    assert [l["codigo"] for l in filtrar_por_producto(lotes, "yogur")] == ["L-001"]
