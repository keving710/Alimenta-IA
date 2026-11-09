"""Registro y validacion de lotes de produccion (RF-01, RF-02, RF-03, RNF-01)."""
import csv
from datetime import date


def validar_lote(producidas, defectuosas):
    """Valida las cantidades de un lote y devuelve el porcentaje de defectos."""
    for valor in (producidas, defectuosas):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise ValueError("Las cantidades deben ser numeros enteros")
    if producidas <= 0:
        raise ValueError("Las unidades producidas deben ser mayores que cero")
    if defectuosas < 0:
        raise ValueError("Las unidades defectuosas no pueden ser negativas")
    if defectuosas > producidas:
        raise ValueError("Las defectuosas no pueden superar a las producidas")
    return 100 * defectuosas / producidas


def registrar_lote(lotes, codigo, fecha, producto, producidas, defectuosas, temperatura):
    """Agrega un lote a la lista `lotes` despues de validarlo y lo devuelve."""
    codigo = str(codigo).strip()
    if not codigo:
        raise ValueError("El codigo de lote es obligatorio")
    if any(l["codigo"] == codigo for l in lotes):
        raise ValueError(f"El codigo de lote {codigo} ya existe")
    try:
        fecha_iso = date.fromisoformat(str(fecha)).isoformat()
    except ValueError:
        raise ValueError("La fecha debe tener formato AAAA-MM-DD")
    producto = str(producto).strip()
    if not producto:
        raise ValueError("El producto es obligatorio")
    if isinstance(temperatura, bool) or not isinstance(temperatura, (int, float)):
        raise ValueError("La temperatura debe ser numerica")
    validar_lote(producidas, defectuosas)

    lote = {
        "codigo": codigo,
        "fecha": fecha_iso,
        "producto": producto,
        "producidas": producidas,
        "defectuosas": defectuosas,
        "temperatura": float(temperatura),
    }
    lotes.append(lote)
    return lote


def filtrar_por_producto(lotes, producto):
    """Devuelve los lotes de un producto (sin distinguir mayusculas)."""
    buscado = producto.strip().lower()
    return [l for l in lotes if l["producto"].lower() == buscado]


def cargar_lotes(ruta):
    """Lee un CSV de lotes. Si trae la columna es_atipico la conserva como int."""
    lotes = []
    with open(ruta, newline="", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            lote = registrar_lote(
                lotes,
                fila["codigo"],
                fila["fecha"],
                fila["producto"],
                int(fila["producidas"]),
                int(fila["defectuosas"]),
                float(fila["temperatura"]),
            )
            if "es_atipico" in fila and fila["es_atipico"] != "":
                lote["es_atipico"] = int(fila["es_atipico"])
    return lotes
