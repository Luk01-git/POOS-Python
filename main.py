from paciente import Paciente
pacientes:list[Paciente]=[]

def leer_numero(mensaje:str)->int:
    while True:
        try:
            numero=int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def menu():
    print("="*20)
    print("Menú de opciones:")
    print("="*20)
    print("1. Agregar paciente")
    print("2. Editar pacientes")
    print("3. Eliminar un paciente")
    print("4. Mostrar un paciente")
    print("5. Mostrar todos los pacientes")
    print("0. Salir")
    opcion=leer_numero("Ingrese el número de la opción deseada: ")
    print("="*20)
    return opcion

def agregar_paciente()-> None:
    rut=input("Ingrese el RUT del paciente: ")
    nombre=input("Ingrese el nombre del paciente: ")
    edad=leer_numero("Ingrese la edad del paciente: ")
    print("Seleccione la previsión del paciente:")
    print("1. Fonasa")
    print("2. Isapre")
    print("3. Particular")
    print("4. Otro")
    opcion=leer_numero("Ingrese el número de la previsión del paciente: ")
    if opcion==1:
        prevision="Fonasa"
    elif opcion==2:
        prevision="Isapre"
    elif opcion==3:
        prevision="Particular"
    elif opcion==4:
        prevision="Otro"
    else:
        print("Opción inválida. Se asignará 'Otro' como previsión por defecto.")
        prevision="Otro"

    paciente=Paciente(rut,nombre,edad,prevision)
    pacientes.append(paciente)
    print("Paciente agregado exitosamente.")
    print(f"Total de pacientes registrados: {len(pacientes)}")
    
def main():
    while True:
        opcion=menu()
        if opcion==1:
            agregar_paciente()
        elif opcion==2:
            print("Editar pacientes")
        elif opcion==3:
            print("Eliminar un paciente")
        elif opcion==4:
            print("Mostrar un paciente")
        elif opcion==5:
            print("Mostrar todos los pacientes")
        elif opcion==0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.")




if __name__=="__main__":
    main()