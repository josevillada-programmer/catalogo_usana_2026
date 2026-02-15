import json
from datetime import datetime

def cargar_catalogo():
    try:
        with open('productos.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Error: No se encontró productos.json. Corre primero el script generador.")
        return {}

def generar_ticket_whatsapp(articulos, total):
    fecha_hoy = datetime.now().strftime("%d/%m/%Y")
    ticket =  "\n*--- COPIA DESDE AQUÍ ---*\n\n"
    ticket += "🌿 *RECIBO DE COMPRA USANA*\n"
    ticket += "------------------------------------------\n"
    ticket += f"📅 *Fecha:* {fecha_hoy}\n\n"
    ticket += "📦 *Detalle de tu pedido:*\n"
    
    for art in articulos:
        ticket += f"• {art['cant']}x {art['nombre']} -> *${art['subtotal']:,.2f}*\n"
    
    ticket += "\n------------------------------------------\n"
    ticket += f"💰 *TOTAL A PAGAR: ${total:,.2f}*\n"
    ticket += "------------------------------------------\n"
    ticket += "¡Gracias por invertir en tu salud! ✨\n"
    ticket += "_Cualquier duda con tu dosis, avísame._"
    ticket += "\n\n*--- HASTA AQUÍ ---*"
    return ticket

def ejecutar_sistema():
    catalogo = cargar_catalogo()
    if not catalogo: return

    carrito = []
    total_venta = 0
    ganancia_neta = 0
    lista_para_ticket = []

    print("=== ASISTENTE DE VENTAS USANA 2026 ===")
    
    while True:
        codigo = input("\nCódigo del producto (o 'fin' para cerrar venta): ")
        if codigo.lower() == 'fin': break
        
        if codigo in catalogo:
            prod = catalogo[codigo]
            try:
                cant = int(input(f"¿Cuántas unidades de {prod['desc']}?: "))
                subtotal = prod['pub'] * cant
                ganancia = (prod['pub'] - prod['pref']) * cant
                
                lista_para_ticket.append({
                    'nombre': prod['desc'],
                    'cant': cant,
                    'subtotal': subtotal
                })
                
                total_venta += subtotal
                ganancia_neta += ganancia
                print(f"✅ Añadido: {prod['desc']}")
            except ValueError:
                print("❌ Cantidad no válida.")
        else:
            print("❌ Código no encontrado.")

    if total_venta > 0:
        print(f"\n💵 Resumen interno: Venta ${total_venta:,.2f} | Ganancia ${ganancia_neta:,.2f}")
        
        opcion = input("\n¿Generar ticket para WhatsApp? (s/n): ")
        if opcion.lower() == 's':
            print(generar_ticket_whatsapp(lista_para_ticket, total_venta))

if __name__ == "__main__":
    ejecutar_sistema()