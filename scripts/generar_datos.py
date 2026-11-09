"""Genera data/lotes_ejemplo.csv con datos sinteticos (semilla fija)."""
import csv
from datetime import date, timedelta

import numpy as np

rng = np.random.default_rng(7)
productos = ["Galletas", "Yogur", "Salsa de tomate"]
N = 60
atipicos = {4: "defectos", 11: "temp_alta", 17: "defectos", 23: "temp_baja", 29: "defectos",
            34: "temp_alta", 41: "defectos", 48: "temp_baja", 55: "volumen"}

filas = []
inicio = date(2026, 9, 1)
for i in range(N):
    prod = productos[i % 3]
    producidas = int(rng.normal(1000, 70))
    tasa = float(np.clip(rng.normal(3.0, 0.8), 0.8, 5.5))
    temp = float(rng.normal(72, 1.8))
    tipo = atipicos.get(i)
    if tipo == "defectos":
        tasa = float(rng.uniform(11, 17))
    elif tipo == "temp_alta":
        temp = float(rng.uniform(86, 93))
    elif tipo == "temp_baja":
        temp = float(rng.uniform(52, 58))
    elif tipo == "volumen":
        producidas = int(rng.uniform(280, 350))
        tasa = float(rng.uniform(8, 10))
    defectuosas = int(round(producidas * tasa / 100))
    filas.append({
        "codigo": f"L-{i + 1:03d}",
        "fecha": (inicio + timedelta(days=i)).isoformat(),
        "producto": prod,
        "producidas": producidas,
        "defectuosas": defectuosas,
        "temperatura": round(temp, 1),
        "es_atipico": 1 if tipo else 0,
    })

with open("data/lotes_ejemplo.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
    w.writeheader()
    w.writerows(filas)
print(f"{len(filas)} lotes generados, {sum(f['es_atipico'] for f in filas)} atipicos")
