import os

x = 0
y = 0
campus = ["zona core", "campus uno", "campus matriz", "sector outsourcing"]

while True:
    os.system("clear")  # Cambio aquí de cls a clear
    print("¿Qué quiere hacer?")
    print("1. Ver los dispositivos.\n2. Ver los campus.\n3. Añadir dispositivo.\n4. Añadir campus.\n5. Borrar dispositivo.\n6. Borrar campus")
    selector = int(input("Elija una opción: "))
    
    if selector == 1:
        y = 1
        print("Elija un campus\n")
        while len(campus) >= y:
            for item in campus:
                print(str(y) + ".", item)
                y += 1
        selector = int(input("\nElija una opción: "))
        x = selector - 1
        if x >= 0:
            try:
                file = open(campus[int(x)] + ".txt", "r")
                for item in file:
                    item = item.strip()
                    print(item)
                file.close()
            except FileNotFoundError:
                print("No se encontró ningún dispositivo para este campus.")
        input("\nPresione Enter para volver al menú principal.")

    elif selector == 2:
        y = 1
        while len(campus) >= y:
            for item in campus:
                print(str(y) + ".", item)
                y += 1
        input("\nPresione Enter para volver al menú principal.")

    elif selector == 3:
        y = 1
        servicios = []
        print("¿Dónde agregar nuevo dispositivo?\n")
        while len(campus) >= y:
            for item in campus:
                print(str(y) + ".", item)
                y += 1
        selector = int(input("\nElija una opción: "))
        x = selector - 1
        if x >= 0:
            file = open(campus[x] + ".txt", "a")
            print("Elija un dispositivo:\n")
            print("1. Router.\n2. Switch.\n3. Switch multicapa.\n")
            variable1 = int(input("Elija su opción: "))
            variable2 = input("Agregue el nombre de su dispositivo: ")
            variable3 = input("Ingrese la dirección IP del dispositivo: ")
            print("¿Cuántas VLANs tiene configuradas el dispositivo?")
            num_vlans = int(input("Ingrese el número de VLANs: "))
            vlans = []
            for i in range(num_vlans):
                vlan = input(f"Ingrese el nombre de la VLAN {i+1}: ")
                vlans.append(vlan)
            print("Servicios de red comprometidos:")
            print("1. DHCP\n2. DNS\n3. Firewall\n4. Proxy\n5. VPN")
            servicios_red = []
            while True:
                opcion_servicio = input("Elija un servicio o 'done' para terminar: ")
                if opcion_servicio == 'done':
                    break
                servicios_red.append(opcion_servicio)
            print("Jerarquía del dispositivo:")
            print("1. Núcleo\n2. Acceso\n3. Distribución")
            jerarquia = int(input("Elija la jerarquía del dispositivo: "))
            file.write("\n---------------------------------\n")
            if variable1 == 1:
                tipo_dispositivo = "Router"
            elif variable1 == 2:
                tipo_dispositivo = "Switch"
            elif variable1 == 3:
                tipo_dispositivo = "Switch multicapa"
            file.write(f"Tipo de dispositivo: {tipo_dispositivo}\n")
            file.write(f"Nombre del dispositivo: {variable2}\n")
            file.write(f"Dirección IP: {variable3}\n")
            file.write(f"VLANs configuradas: {', '.join(vlans)}\n")
            file.write(f"Servicios de red comprometidos: {', '.join(servicios_red)}\n")
            if jerarquia == 1:
                file.write("Jerarquía: Núcleo\n")
            elif jerarquia == 2:
                file.write("Jerarquía: Acceso\n")
            elif jerarquia == 3:
                file.write("Jerarquía: Distribución\n")
            file.write("---------------------------------\n")
            file.close()
        input("\nPresione Enter para volver al menú principal.")

    elif selector == 4:
        print("Ingrese el nombre del nuevo campus:")
        nuevo_campus = input()
        campus.append(nuevo_campus)
        print("¡Campus añadido con éxito!")
        input("\nPresione Enter para volver al menú principal.")

    elif selector == 5:
        print("¿Dónde desea borrar dispositivos?")
        for i, c in enumerate(campus, start=1):
            print(f"{i}. {c}")
        opcion = int(input())
        if 1 <= opcion <= len(campus):
            campus_name = campus[opcion - 1]
            try:
                os.remove(campus_name + ".txt")
                print(f"Dispositivos de {campus_name} eliminados con éxito.")
            except FileNotFoundError:
                print(f"No se encontraron dispositivos para {campus_name}.")
        else:
            print("¡Opción inválida!")
        input("\nPresione Enter para volver al menú principal.")

    elif selector == 6:
        print("¿Qué campus desea eliminar?")
        for i, c in enumerate(campus, start=1):
            print(f"{i}. {c}")
        opcion = int(input())
        if 1 <= opcion <= len(campus):
            campus.pop(opcion - 1)
            print("¡Campus eliminado con éxito!")
        else:
            print("¡Opción inválida!")
        input("\nPresione Enter para volver al menú principal.")
