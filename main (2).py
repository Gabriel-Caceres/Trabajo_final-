from random import randint

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

meses = ["Enero 2024", "Febrero 2024", "Marzo 2024", "Abril 2024", "Mayo 2024",
         "Junio 2024", "Julio 2024", "Agosto 2024", "Septiembre 2024", "Octubre 2024", "Noviembre 2024", "Diciembre 2024"]

print(dicc)

while opcion != 4:

    if opcion == 1:

    if opcion == 2:

    if opcion == 3:
        busqueda = input("Ingrese el rut del afiliado: ")
        try:
            indice = dicc["Rut"].index(busqueda)
            print("")
            print("-"*50)
            print("CERTIFICADO DE AFILIACION: ISAPRE VIDA Y SALUD")
            print("-"*50)
            for clave, valores in dicc.items():
                print(f"{clave.ljust(20)}: {valores[indice]}")
            print("-"*50)
            for mes in meses:
                print(f"{mes.ljust(20)}: $ {randint(1000,1500)}")
            print("-"*50, "\n")

        except ValueError:
            print("\n *****RUT NO ENCONTRADO*****")

    if opcion == 4:
        print("\nSaliendo del sistema...")
        print("\tVersion SYS 2025-06 v.1")
        print("\tCopy Right")
        print("\tGabriel Barrea | Gabriel Caceres | Jean Indey")
        print("\n****CIERRE EXITOSO****")
        print("")