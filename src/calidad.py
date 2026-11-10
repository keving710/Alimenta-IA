"""Indicadores de calidad de produccion (RF-02, RF-04)."""
from src.produccion import validar_lote


def tasa_lote(lote):
    return validar_lote(lote["producidas"], lote["defectuosas"])


def resumen(lotes):
    if not lotes:
        return {
            "total_lotes": 0,
            "unidades_producidas": 0,
            "unidades_defectuosas": 0,
            "tasa_global": 0.0,
            "tasa_promedio_lotes": 0.0,
            "lote_mayor_tasa": None,
        }
    producidas = sum(l["producidas"] for l in lotes)
    defectuosas = sum(l["defectuosas"] for l in lotes)
    tasas = [tasa_lote(l) for l in lotes]
    peor = max(lotes, key=tasa_lote)
    return {
        "total_lotes": len(lotes),
        "unidades_producidas": producidas,
        "unidades_defectuosas": defectuosas,
        "tasa_global": 100 * defectuosas / producidas,
        "tasa_promedio_lotes": sum(tasas) / len(tasas),
        "lote_mayor_tasa": peor["codigo"],
    }


def tablero(lotes):
    r = resumen(lotes)
    lineas = [
        "=== TABLERO ALIMENTA-IA ===",
        f"Lotes registrados:        {r['total_lotes']}",
        f"Unidades producidas:      {r['unidades_producidas']}",
        f"Unidades defectuosas:     {r['unidades_defectuosas']}",
        f"Tasa global de defectos:  {r['tasa_global']:.2f}%",
        f"Tasa promedio por lote:   {r['tasa_promedio_lotes']:.2f}%",
        f"Lote con mayor tasa:      {r['lote_mayor_tasa']}",
    ]
    return "\n".join(lineas)
