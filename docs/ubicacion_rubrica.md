# Ubicacion de la rubrica en el repositorio - ALIMENTA-IA

Equipo: Kevin A. Gañan (keving710) y Juan Diego Ruiz (mposada1-creator)

Repositorio: https://github.com/keving710/Alimenta-IA

Este documento indica donde esta el contenido de cada criterio de evaluacion del taller. Las rutas son relativas a la raiz del repositorio (rama `main`).

## 1. Requisitos, riesgos y plan de calidad (20 puntos)

| Contenido | Ubicacion |
|---|---|
| Matriz de requisitos funcionales y no funcionales (RF-01 a RF-05, RNF-01 a RNF-04) con criterios de aceptacion | `docs/requisitos.md` |
| Roles del equipo | `docs/requisitos.md` (inicio) |
| Tres riesgos priorizados (probabilidad x impacto) | `docs/requisitos.md` (seccion "Riesgos priorizados") |
| Plan de calidad: objetivos, controles preventivos, pruebas, responsables, criterios de salida y registro de defectos | `docs/plan_calidad.md` |

## 2. Gestion de configuracion Git/GitHub y trazabilidad (25 puntos)

| Contenido | Ubicacion |
|---|---|
| Elementos de configuracion (SCI), lineas base, convenciones de ramas, commits y PR, registro de cambios | `docs/plan_configuracion.md` |
| Trazabilidad RF -> ticket -> rama -> commit -> PR -> prueba -> resultado | `docs/informe_auditoria.md` (seccion 3) y `docs/plan_configuracion.md` |
| Ramas, commits, historial y Pull Requests (#1, #2 y #3) | GitHub: pestanas *Code*, *Commits* y *Pull requests* |
| Tag y release v1.0.0 | GitHub: pestanas *Tags* y *Releases* |

## 3. Implementacion y pruebas verificables (20 puntos)

| Contenido | Ubicacion |
|---|---|
| Registro y validacion de lotes (RF-01, RF-02, RF-03, RNF-01) | `src/produccion.py` |
| Indicadores y tablero (RF-02, RF-04) | `src/calidad.py` y `src/app.py` |
| Deteccion de lotes atipicos con IA (RF-05) | `src/detector_ia.py` |
| Pruebas automaticas con pytest (18 pruebas) | `tests/test_produccion.py`, `tests/test_calidad.py`, `tests/test_detector_ia.py` |
| Resultado de las pruebas | `docs/informe_auditoria.md` (seccion 1) y capturas de `python -m pytest -q` |
| Instrucciones para instalar y ejecutar | `README.md` |
| Dependencias | `requirements.txt` |

## 4. Metricas, analisis e IA responsable (25 puntos)

| Contenido | Ubicacion |
|---|---|
| Plan de medicion: indicadores, formulas, fuentes, metas y responsables | `docs/plan_medicion.md` |
| Matriz de medicion y analisis con los valores obtenidos | `docs/informe_auditoria.md` (seccion 1) |
| Datos sinteticos etiquetados (60 lotes, 9 atipicos) | `data/lotes_ejemplo.csv` |
| Script que genera los datos (semilla fija) | `scripts/generar_datos.py` |
| Detector de IA, semilla, parametros y evaluacion (recall y precision) | `src/detector_ia.py` |
| Aviso de uso orientativo y limitaciones de la IA | `src/detector_ia.py` (constante `AVISO`), `README.md`, `docs/plan_medicion.md` y `docs/informe_auditoria.md` |

## 5. Auditoria, decision y comunicacion (10 puntos)

| Contenido | Ubicacion |
|---|---|
| Checklist de auditoria | `docs/informe_auditoria.md` (seccion 2) |
| Defectos y desviaciones de proceso | `docs/informe_auditoria.md` (seccion 4) y `docs/plan_calidad.md` |
| Decision de liberacion (aprobar / aplazar) con evidencias | `docs/informe_auditoria.md` (seccion 5) |
| Retrospectiva | `docs/informe_auditoria.md` (seccion 6) |
| Notas de version | `docs/notas_version_v1.0.0.md` y la pagina del release v1.0.0 en GitHub |

## Resumen de entregables

| Entregable | Ubicacion |
|---|---|
| URL del repositorio GitHub | https://github.com/keving710/Alimenta-IA |
| Documentos de calidad, medicion y configuracion | `docs/` |
| Codigo y pruebas | `src/` y `tests/` |
| CSV sintetico | `data/lotes_ejemplo.csv` |
| PR con revision | GitHub, pestana *Pull requests* (#1, #2 y #3) |
| Informe de indicadores y auditoria | `docs/informe_auditoria.md` |
| Release v1.0.0 | GitHub, pestana *Releases* |
