"""Interfaz de linea de comandos de ALIMENTA-IA.

Uso:
    python -m src.app                 # tablero + alertas
    python -m src.app Yogur           # filtra por producto
"""
import os
import sys

from src import calidad, detector_ia, produccion

RUTA_DATOS = os.path.join(os.path.dirname(__file__), "..", "data", "lotes_ejemplo.csv")


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    lotes = produccion.cargar_lotes(RUTA_DATOS)

    if argv:
        lotes_vista = produccion.filtrar_por_producto(lotes, argv[0])
        print(f"Producto filtrado: {argv[0]} ({len(lotes_vista)} lotes)")
    else:
        lotes_vista = lotes

    print(calidad.tablero(lotes_vista))

    modelo = detector_ia.entrenar(lotes)
    marcados = detector_ia.marcar_lotes(modelo, lotes_vista)
    alertas = [l for l in marcados if l["alerta_ia"] == 1]
    print(f"\nLotes con alerta de IA: {len(alertas)} de {len(marcados)}")
    for l in alertas:
        print(f"  - {l['codigo']} ({l['producto']}): defectos {calidad.tasa_lote(l):.1f}%, "
              f"temp {l['temperatura']:.1f} C")
    print("\n" + detector_ia.AVISO)

    if all("es_atipico" in l for l in lotes):
        ev = detector_ia.evaluar(lotes)
        print(f"\nEvaluacion (conjunto de prueba, n={ev['n_prueba']}): "
              f"recall={ev['recall']:.2f}, precision={ev['precision']:.2f}")


if __name__ == "__main__":
    main()
