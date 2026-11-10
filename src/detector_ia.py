"""Deteccion de lotes atipicos con IsolationForest (RF-05)."""
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from src.calidad import tasa_lote

SEMILLA = 42
CONTAMINACION = 0.15
AVISO = (
    "AVISO: una alerta de IA es solo una indicacion orientativa de que el lote "
    "se aparta del comportamiento habitual. No implica defecto ni riesgo "
    "sanitario y no reemplaza el control de calidad ni al profesional responsable."
)


def _matriz(lotes):
    return np.array([[l["producidas"], tasa_lote(l), l["temperatura"]] for l in lotes])


def entrenar(lotes, contaminacion=CONTAMINACION, semilla=SEMILLA):
    modelo = make_pipeline(
        StandardScaler(),
        IsolationForest(n_estimators=200, contamination=contaminacion, random_state=semilla),
    )
    modelo.fit(_matriz(lotes))
    return modelo


def detectar(modelo, lotes):
    pred = modelo.predict(_matriz(lotes))
    return [1 if p == -1 else 0 for p in pred]


def marcar_lotes(modelo, lotes):
    marcas = detectar(modelo, lotes)
    return [dict(l, alerta_ia=m) for l, m in zip(lotes, marcas)]


def evaluar(lotes, semilla=SEMILLA, prop_prueba=0.3):
    etiquetas = [l["es_atipico"] for l in lotes]
    entrena, prueba = train_test_split(
        lotes, test_size=prop_prueba, random_state=semilla, stratify=etiquetas
    )
    modelo = entrenar(entrena, semilla=semilla)
    real = [l["es_atipico"] for l in prueba]
    pred = detectar(modelo, prueba)
    tp = sum(1 for r, p in zip(real, pred) if r == 1 and p == 1)
    fn = sum(1 for r, p in zip(real, pred) if r == 1 and p == 0)
    fp = sum(1 for r, p in zip(real, pred) if r == 0 and p == 1)
    return {
        "n_entrenamiento": len(entrena),
        "n_prueba": len(prueba),
        "atipicos_en_prueba": sum(real),
        "tp": tp,
        "fn": fn,
        "fp": fp,
        "recall": recall_score(real, pred, zero_division=0),
        "precision": precision_score(real, pred, zero_division=0),
    }
