import os

from src import detector_ia
from src.produccion import cargar_lotes

RUTA = os.path.join(os.path.dirname(__file__), "..", "data", "lotes_ejemplo.csv")


def test_dataset_tiene_al_menos_30_lotes_y_atipicos():
    lotes = cargar_lotes(RUTA)
    assert len(lotes) >= 30
    assert 0 < sum(l["es_atipico"] for l in lotes) < len(lotes)


def test_alerta_en_lote_claramente_atipico():
    lotes = cargar_lotes(RUTA)
    modelo = detector_ia.entrenar(lotes)
    raro = {"codigo": "X", "fecha": "2026-10-01", "producto": "Yogur",
            "producidas": 1000, "defectuosas": 200, "temperatura": 95.0}
    assert detector_ia.detectar(modelo, [raro]) == [1]


def test_resultados_reproducibles_con_semilla():
    lotes = cargar_lotes(RUTA)
    assert detector_ia.evaluar(lotes) == detector_ia.evaluar(lotes)


def test_evaluacion_devuelve_metricas_validas():
    ev = detector_ia.evaluar(cargar_lotes(RUTA))
    assert 0 <= ev["recall"] <= 1
    assert ev["tp"] + ev["fn"] == ev["atipicos_en_prueba"]


def test_aviso_de_uso_orientativo():
    assert "orientativa" in detector_ia.AVISO
