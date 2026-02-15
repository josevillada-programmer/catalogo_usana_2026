import json
from datetime import datetime

def cargar_catalogo():
    try:
        with open('productos.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: No se encontró el archivo productos.json")
        return {}

def guardar_en_historial(resumen):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('historial_ventas.txt', 'a', encoding='utf-8') as f:
        f.write(f"Fecha: {fecha}\n{resumen}\n" + "-"*40 + "\n")

def ejecutar_asistente():
    catalogo = cargar_catalogo()
    if not catalogo: return

    print("\n=== SISTEMA DE GESTIÓN USANA 2026 ===")
    carrito = []
    total_v = 0
    total_p = 0
    ganancia_t = 0

    while True:
        codigo = input("\nCódigo del producto (o 'fin' para cobrar): ")
        if codigo.lower() == 'fin': break
        
        if codigo in catalogo:
            prod = catalogo[codigo]
            try:
                cant = int(input(f"¿Unidades de {prod['desc']}?: "))
                subtotal = prod['pub'] * cant
                ganancia = (prod['pub'] - prod['pref']) * cant
                puntos = prod['pc'] * cant
                
                carrito.append(f"{cant}x {prod['desc']} - ${subtotal:,.2f}")
                total_v += subtotal
                ganancia_t += ganancia
                total_p += puntos
                print(f"✅ Agregado correctamente.")
            except ValueError:
                print("❌ Error: Ingresa un número válido.")
        else:
            print("❌ El código no existe en el catálogo.")

    if total_v > 0:
        resumen_final = (
            f"VENTA TOTAL: ${total_v:,.2f}\n"
            f"GANANCIA NETA: ${ganancia_t:,.2f}\n"
            f"PUNTOS VP: {total_p}"
        )
        
        print("\n" + "="*30)
        print(resumen_final)
        print("="*30)
        
        confirmar = input("¿Guardar esta venta en el historial? (s/n): ")
        if confirmar.lower() == 's':
            # Creamos un bloque de texto con los artículos para el txt
            detalle_articulos = "\n".join(carrito)
            registro = f"Artículos:\n{detalle_articulos}\n{resumen_final}"
            guardar_en_historial(registro)
            print("💾 Venta guardada en historial_ventas.txt")

if __name__ == "__main__":
    ejecutar_asistente()