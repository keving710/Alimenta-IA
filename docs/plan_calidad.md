# Plan de calidad - ALIMENTA-IA

## Objetivos
1. Evitar registros invalidos de lotes.
2. Asegurar que todo cambio sea trazable.
3. Detectar fallas o limitaciones del modelo de IA.
4. Llegar a la version v1.0.0 con pruebas aprobadas y sin defectos criticos abiertos.

## Matriz de controles

| Objetivo de calidad | Control preventivo | Prueba o evidencia | Responsable | Criterio de aceptacion |
|---|---|---|---|---|
| Evitar registros invalidos | Validacion de cantidades, fecha y codigo unico antes de guardar | tests/test_produccion.py (casos normal, cero, negativos, defectuosas > producidas, duplicado, fecha) | Kevin A. Gañan | 100% de pruebas de validacion aprobadas |
| Asegurar cambios trazables | Ticket por cambio, rama `feature/GH-XX`, commits con convencion, PR con revision cruzada | Historial de GitHub, PR vinculados a tickets, matriz de trazabilidad | Juan Diego Ruiz | 100% de PR revisados antes de integrar |
| Detectar fallas de IA | Semilla fija, datos etiquetados, evaluacion separada de entrenamiento, aviso orientativo | tests/test_detector_ia.py y evaluacion de recall/precision | Juan Diego Ruiz | Recall reportado con sus limitaciones; aviso visible en toda alerta |
| Reproducibilidad | requirements.txt con versiones, CSV versionado, script de generacion | Instalacion limpia + `python -m pytest -q` | Kevin A. Gañan | Las pruebas pasan en un entorno nuevo |

## Actividades de QA
- Pruebas unitarias con pytest en cada incremento.
- Revision de codigo por el otro integrante en cada PR (checklist: nombres claros, validaciones, pruebas incluidas, sin secretos).
- Pruebas de regresion completas antes de la liberacion.
- Registro de defectos con severidad (critico, mayor, menor) y estado (abierto, en correccion, cerrado).

## Criterios de salida (liberacion v1.0.0)
- Cero defectos criticos abiertos.
- Todas las pruebas obligatorias aprobadas.
- Todos los PR integrados fueron revisados.
- Sin secretos ni datos reales en el repositorio.
- README, requirements.txt y datos sinteticos presentes.

## Registro de defectos

| ID | Descripcion | Severidad | Estado | Evidencia |
|---|---|---|---|---|
| D-01 |  | | | |
