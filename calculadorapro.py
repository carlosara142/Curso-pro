while True:
    print("===========Calculadora===========")
    print("Opciones: ")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    

    opcion = input("Seleccione una opción (1-4): ")
    if opcion not in ['1', '2', '3', '4']:
        print("Opción inválida. Por favor, seleccione entre 1 y 4.")
        continue    
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: ")) 

    if opcion == '1':
        resultado = a + b
        print(f"El resultado de {a} + {b} es: {resultado}")
    elif opcion == '2':
        resultado = a - b
        print(f"El resultado de {a} - {b} es: {resultado}")
    elif opcion == '3':
        resultado = a * b
        print(f"El resultado de {a} * {b} es: {resultado}")
    elif opcion == '4':
        if b != 0:
            resultado = a / b
            print(f"El resultado de {a} / {b} es: {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    otra = input("¿Desea realizar otra operación? (s/n): ")
    if otra != 's':
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break