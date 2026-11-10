# ALIMENTA-IA

Prototipo educativo para registrar lotes de produccion de la fabrica ficticia NutriAlimentos S.A.S., calcular la tasa de defectos y senalar lotes atipicos con un modelo sencillo de IA. Los datos son sinteticos.

Taller integrador de Administracion de Proyectos de Software (UTP).
Equipo: Kevin A. Gañan y Juan Diego Ruiz.

## Aviso

Las alertas de IA son solo apoyo analitico. No reemplazan los controles de inocuidad, las pruebas de laboratorio ni la decision de los profesionales responsables.

## Estructura

```
src/      app.py, produccion.py, calidad.py, detector_ia.py
tests/    pruebas con pytest
data/     lotes_ejemplo.csv (sintetico, 60 lotes, 9 atipicos etiquetados)
docs/     requisitos, planes de calidad, medicion y configuracion, informe de auditoria
scripts/  generar_datos.py (regenera el CSV con semilla fija)
```

## Instalacion y uso

```
python -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m src.app                # tablero y alertas
python -m src.app Yogur          # filtra por producto
python -m pytest -q              # pruebas
python -m pytest --cov=src       # pruebas con cobertura
```
