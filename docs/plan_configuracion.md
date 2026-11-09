# Plan de configuracion - ALIMENTA-IA

## Elementos de configuracion (SCI)

| ID SCI | Elemento | Ubicacion | Responsable | Version / linea base |
|---|---|---|---|---|
| SCI-01 | Codigo fuente | src/ | Kevin A. Gañan | LB-0 (commit inicial), v1.0.0 |
| SCI-02 | Pruebas | tests/ | Juan Diego Ruiz | LB-0, v1.0.0 |
| SCI-03 | Datos sinteticos | data/ y scripts/generar_datos.py | Juan Diego Ruiz | LB-0, v1.0.0 |
| SCI-04 | Documentacion | docs/ y README.md | Juan Diego Ruiz | LB-0, v1.0.0 |
| SCI-05 | Dependencias | requirements.txt | Kevin A. Gañan | LB-0, v1.0.0 |

## Lineas base
- **LB-0:** estructura inicial del repositorio (commit "chore: estructura inicial ALIMENTA-IA").
- **LB-1:** `main` despues de integrar GH-01, GH-02 y GH-03 y aprobar la regresion.
- **v1.0.0:** tag anotado sobre LB-1.

## Convenciones
- **Ramas:** `main` (estable) y `feature/GH-XX-descripcion`. Nadie hace push directo a `main` despues de la linea base inicial.
- **Commits:** `tipo(GH-XX): descripcion corta`. Tipos: feat, fix, test, docs, chore.
- **Pull Requests:** hacia `main`, con el ticket referenciado en la descripcion, resultado de pytest y revision del otro integrante.
- **Etiquetas:** `vMAYOR.MENOR.PARCHE`, siempre anotadas.

## Control de cambios

| Ticket | Motivo | SCI afectados | Riesgo / impacto | Decision | PR / evidencia |
|---|---|---|---|---|---|
| GH-01 | Registro y validacion de lotes | src/produccion.py, tests/test_produccion.py | Alto: base de todos los calculos | Aprobado si pasan las pruebas | PR #1 (completar enlace) |
| GH-02 | Indicadores y tablero | src/calidad.py, src/app.py, tests/test_calidad.py | Medio | Aprobado si pasan las pruebas | PR #2 (completar enlace) |
| GH-03 | Detector de lotes atipicos con IA | src/detector_ia.py, data/, tests/test_detector_ia.py | Medio: las alertas no deben confundirse con decisiones de inocuidad | Aprobado si pasan las pruebas y se muestra el aviso | PR #3 (completar enlace) |

## Trazabilidad

| Requisito | Ticket | Rama | Pruebas |
|---|---|---|---|
| RF-01, RNF-01 | GH-01 | feature/GH-01-registro-lotes | test_produccion.py |
| RF-02, RF-03 | GH-01 / GH-02 | feature/GH-01-registro-lotes, feature/GH-02-indicadores | test_produccion.py, test_calidad.py |
| RF-04 | GH-02 | feature/GH-02-indicadores | test_calidad.py |
| RF-05 | GH-03 | feature/GH-03-detector-ia | test_detector_ia.py |
| RNF-02 | todos | todas | historial de PR |
| RNF-03 | GH-03 | feature/GH-03-detector-ia | test de reproducibilidad, requirements.txt |
| RNF-04 | GH-00 / auditoria | main | revision de .gitignore y del historial |

(Al terminar, agregar el hash de cada commit y el enlace del PR en esta tabla.)
