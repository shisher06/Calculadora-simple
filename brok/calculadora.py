suma = lambda a, b: a +b
resta = lambda a, b: a-b
multiplicacion = lambda a, b: a*b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

while True:
    operacion = input("¿Qué operación deseas realizar? (+-*/) o 'q' para salir: ").strip()
    
    if operacion.lower() == 'q':
        print("¡Hasta luego!")
        break
    
    if operacion not in ["+", "-", "*", "/"]:
        print("Operación no válida. Por favor, elige entre +, -, *, /.")
        continue
    
    numeros = input("Con qué números quieres realizar la operación? (a,b): ").split(',')
    
    if len(numeros) != 2:
        print("Por favor, ingresa exactamente dos números separados por coma.")
        continue
    
    try:
        a, b = map(float, numeros)
    except ValueError:
        print("Por favor, ingresa números válidos.")
        continue
    
    if operacion == "+":
        resultado = suma(a, b)
    elif operacion == "-":
        resultado = resta(a, b)
    elif operacion == "*":
        resultado = multiplicacion(a, b)
    elif operacion == "/":
        resultado = division(a, b)
    
    print(f"El resultado es: {resultado}")