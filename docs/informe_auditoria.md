# Informe de indicadores y auditoria - ALIMENTA-IA

Fecha: 6 / 11 / 2026   Equipo: Kevin A. Gañan, Juan Diego Ruiz
NOTA IMPORTANTE: PARA PODER VER EL DOC DE INFORME DE MANERA CORRECTA CTRL+SHIFT+V 
## 1. Matriz de medicion y analisis

| Indicador | Valor obtenido | Meta | Interpretacion | Accion correctiva |
|---|---|---|---|---|
| Aprobacion de pruebas | 18 / 18 = 100% (ejecutado en la regresion local; actualizar si se agregan pruebas) | 100% | Se cumple la meta | Ninguna |
| Cobertura de requisitos | 5 RF con pruebas / 5 RF = 100% (RF-01 a RF-05) | >= 90% | Todos los RF funcionales tienen al menos una prueba. RNF-02 y RNF-04 se verifican por revision y no por pytest | Agregar una verificacion automatica de secretos en una version futura |
| PR revisados | 3 / 3 = 100% | 100% | | |
| Cumplimiento del proyecto | 5 / 6 = 83,3% | >= 80% | a la fecha falta el tag y el release | Implementarlo en los siguientes dias antes de la entrega final 
| Tasa de defectos de produccion | Global 3.65% (2140 de 58669 unidades), promedio por lote 3.69%; lote con mayor tasa: L-030 (15.5%) | Analizar tendencia | Sin meta industrial real; los lotes con tasas de 10% o mas coinciden con los atipicos sinteticos | Revisar manualmente los lotes con alerta |
| Evaluacion de IA | Recall 1.00 y precision 1.00 en prueba (3 TP, 0 FN, 0 FP de 18 lotes). Sobre los 60 lotes el modelo marco 9 alertas, igual al numero de atipicos etiquetados | Reportar valor y limitaciones | El resultado es bueno pero poco confiable estadisticamente: muestra de prueba de 18 lotes, atipicos inyectados y marcados | Probar con mas lotes, otras semillas y anomalias mas sutiles |

Nota sobre las dos tasas: el 3.65% (global) pondera por unidades; el 3.69% es el promedio simple de las tasas por lote. Difieren porque los lotes no tienen el mismo tamano.

## 2. Checklist de auditoria

- [ x ] Requisitos aprobados y versionados (docs/requisitos.md en main)
- [ x ] Ramas y commits con convencion
- [ x ] PR revisados y vinculados a tickets
- [ x ] Pruebas ejecutadas con evidencia (captura de `python -m pytest -q`)
- [ x ] Dependencias y datos reproducibles (instalacion en entorno limpio)
- [ x ] Sin secretos ni datos sensibles (.gitignore y revision del historial)
- [ x ] Reporte de metricas y analisis
- [ ] Tag y notas de release coherentes



## 3. Trazabilidad auditada

| Requisito | Ticket | Rama | Commit | PR | Prueba | Resultado |
|---|---|---|---|---|---|---|
| RF-01 / RNF-01 | GH-01 | feature/GH-01-registro-lotes | | | test_produccion.py | Aprobado |
| RF-02 / RF-03 | GH-01 / GH-02 | | | | test_produccion.py, test_calidad.py | Aprobado |
| RF-04 | GH-02 | feature/GH-02-indicadores | | | test_calidad.py | Aprobado |
| RF-05 | GH-03 | feature/GH-03-detector-ia | | | test_detector_ia.py | Aprobado |

## 4. Defectos encontrados
Ver registro en docs/plan_calidad.md. Defectos criticos abiertos:

## 5. Decision de liberacion

Criterios: cero defectos criticos abiertos, pruebas obligatorias aprobadas y PR revisados.

Decision: [ x ] Aprobar v1.0.0   [ ] Aplazar

Justificacion: Se realizan pruebas a cada modulo, se valido cada PR y app funciona bien.

## 6. Retrospectiva breve
- Que funciono bien:
- Que mejorariamos:
- Limites del prototipo: datos sinteticos, IA solo orientativa, CLI en lugar de interfaz web.
