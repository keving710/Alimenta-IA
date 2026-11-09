# Requisitos y riesgos - ALIMENTA-IA

Roles del equipo (2 integrantes):

| Rol | Responsable |
|---|---|
| Product Owner | Kevin A. Gañan |
| Desarrollador | Kevin A. Gañan (GH-01, GH-03) y Juan Diego Ruiz (GH-02) |
| Responsable QA | Juan Diego Ruiz |
| Configuracion y medicion | Juan Diego Ruiz |

Como somos dos, cada PR lo revisa la persona que no lo escribio.

## Matriz de requisitos

| ID | Requisito | Criterio de aceptacion | Prioridad | Modulo |
|---|---|---|---|---|
| RF-01 | Registrar lote | Se guarda con codigo unico, fecha valida, producto y cantidades validas; un codigo repetido se rechaza | Alta | src/produccion.py |
| RF-02 | Calcular % de defectos | (defectuosas / producidas) x 100; 200 producidas y 6 defectuosas da 3.0 | Alta | src/produccion.py, src/calidad.py |
| RF-03 | Consultar historial y filtrar | Se pueden listar los lotes cargados y filtrar por producto sin importar mayusculas | Media | src/produccion.py |
| RF-04 | Tablero | Muestra conteo de lotes y tasa de defectos (global y promedio) | Media | src/calidad.py, src/app.py |
| RF-05 | Marcar lotes atipicos | Se marcan lotes atipicos con IsolationForest y siempre se muestra el aviso de uso orientativo | Alta | src/detector_ia.py |
| RNF-01 | Validacion de cantidades | No se aceptan negativos ni defectuosas > producidas | Alta | src/produccion.py |
| RNF-02 | Cambios trazables | Cada cambio integrado tiene ticket, PR y pruebas asociadas | Alta | GitHub |
| RNF-03 | Reproducibilidad | Dependencias fijadas en requirements.txt, datos de prueba versionados y semilla fija en la IA | Media | requirements.txt, data/ |
| RNF-04 | Sin secretos ni datos reales | El repositorio no contiene credenciales ni datos sensibles; .gitignore revisado | Alta | .gitignore |

## Riesgos priorizados

Escala 1 a 5 para probabilidad (P) e impacto (I).

| # | Riesgo | P | I | Exposicion (PxI) | Respuesta |
|---|---|---|---|---|---|
| R1 | Se aceptan datos invalidos (negativos, defectuosas > producidas) y se calculan tasas erroneas | 3 | 5 | 15 | Validacion en `validar_lote` y pruebas de casos limite (RNF-01) |
| R2 | Cambios integrados a `main` sin revision ni pruebas, que dejan la version inestable | 3 | 4 | 12 | Rama por ticket, PR obligatorio con revision cruzada, pytest antes de integrar |
| R3 | La IA genera falsas alarmas o deja pasar lotes anomalos y se toma como decision de inocuidad | 3 | 4 | 12 | Aviso de uso orientativo, reporte de recall/precision con sus limites, semilla fija |

Riesgo adicional anotado pero no priorizado: la hoja de datos es muy pequena (60 lotes), por lo que las metricas de la IA son poco estables.
