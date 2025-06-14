opcion = 0

est_civil = {"C":"Casado",
             "S":"Soltero",
             "V":"Viudo"}

generos = {"M":"Masculino",
           "F":"Femenino",}

dicc = {"Rut": [],
        "Nombre": [],
        "Edad": [],
        "Estado Civil": [],
        "Genero": [],
        "fecha": []}

print(dicc)

while opcion != 4:

    if opcion == 1:

    if opcion == 2:
        while True :
            busqueda = input("\ningrese el rut de la persona que desea buscar Ej(11.111.111-1) : \n")
            try:
                indice = dicc["Rut"].index(busqueda)
                for clave, valores in dicc.items():
                    print(f"{clave.ljust(20)}: {valores[indice]}")
            except ValueError:
                print("\n RUT no encontrado.")
            try:    
                Respuesta = str(input("\nDesea realizar otra busqueda (SI/NO): \n")).upper()
            except ValueError:
                print("debe ingresar solo caracteres")
            if Respuesta == "NO":
                break
            else:
                print("Ingreso no valido")              

    if opcion == 3:

    if opcion == 4: