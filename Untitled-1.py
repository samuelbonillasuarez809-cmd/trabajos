
saldo = 1000.0 
pin_correcto = "1234"
intentos = 3

print("Banco python")

while intentos > 0:
        entrada_pin = input("Ingrese su PIN de 4 dígitos: ")
        if entrada_pin == pin_correcto:
            print("\nAcceso concedido.")
            break
        else:
            intentos -= 1
            print(f"PIN incorrecto. Le quedan {intentos} intentos.")
            if intentos == 0:
                print("Tarjeta bloqueada. Contacte a su banco.")

while True:
        print("\n--- MENÚ DE OPERACIONES ---")
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"\nSu saldo actual es: ${saldo:.2f}")

        elif opcion == "2":
            deposito = float(input("Ingrese la cantidad a depositar: "))
            if deposito > 0:
                saldo += deposito
                print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
            else:
                print("Cantidad no válida.")

        elif opcion == "3":
            retiro = float(input("Ingrese la cantidad a retirar: "))
            if retiro > saldo:
                print("Fondos insuficientes.")
            elif retiro <= 0:
                print("Cantidad no válida.")
            else:
                saldo -= retiro
                print(f"Retiro exitoso. Saldo restante: ${saldo:.2f}")

        elif opcion == "4":
            print("Gracias por usar nuestro cajero. ¡Hasta pronto!")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")