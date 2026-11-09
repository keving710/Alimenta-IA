# Plan de medicion y analisis - ALIMENTA-IA

Se separan cuatro ambitos para no mezclar los defectos del software con las unidades defectuosas de la fabrica.

| Ambito | Indicador | Formula / metodo | Fuente | Meta | Responsable |
|---|---|---|---|---|---|
| Producto (software) | Aprobacion de pruebas | pruebas aprobadas / ejecutadas x 100 | salida de pytest | 100% de las obligatorias | Juan Diego Ruiz |
| Producto (software) | Cobertura de requisitos | RF con pruebas / RF totales x 100 | matriz de trazabilidad | >= 90% | Juan Diego Ruiz |
| Proceso | PR revisados | PR aprobados / PR integrados x 100 | GitHub | 100% | Juan Diego Ruiz |
| Proyecto | Cumplimiento | tareas terminadas / comprometidas x 100 | lista de tickets GH-01..GH-03 y tareas de documentacion | >= 80% | Kevin A. Gañan |
| Produccion | Tasa de defectos por lote y global | defectuosas / producidas x 100 | data/lotes_ejemplo.csv | Analizar tendencia (sin meta industrial real) | Kevin A. Gañan |
| IA | Recall de anomalias | TP / (TP + FN) con etiquetas de prueba | conjunto de prueba (30%) del CSV etiquetado | Reportar valor y limitaciones | Kevin A. Gañan |

## Como se calcula cada cosa
- `python -m pytest -q` entrega el numero de pruebas aprobadas.
- `python -m pytest --cov=src` entrega la cobertura de codigo (dato complementario, distinto a la cobertura de requisitos).
- La tasa de defectos sale de `python -m src.app`.
- La evaluacion de IA sale de `detector_ia.evaluar()`: separacion estratificada 70/30, semilla 42, contaminacion 0.15, variables escaladas (unidades producidas, tasa de defectos y temperatura).

## Limitaciones de la medicion de IA
- Con 60 lotes, el conjunto de prueba tiene solo 18 lotes y 3 atipicos, por lo que un solo acierto o fallo cambia mucho el recall.
- Los atipicos del CSV fueron inyectados por nosotros y son relativamente marcados; en datos reales las anomalias serian mas sutiles.
- Una anomalia estadistica no es por si sola un defecto ni un riesgo sanitario.
