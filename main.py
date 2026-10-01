from departamento import Departamento
from paciente import Paciente
pacientes:list[Paciente]=[]

def leer_numero(mensaje:str)->int:
    while True:
        try:
            numero=int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def imprimir_pacientes()->None:
    if len(pacientes)==0:
        print("No hay pacientes.")
    else:
        for paciente in pacientes:
            print(paciente)
            print("="*20)



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
    opcion=leer_numero("Ingrese opción: ")
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
    try:
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
        try:
            paciente=Paciente(rut,nombre,edad,prevision)
        except (TypeError, ValueError) as e:
            print(f"Error al crear el paciente: {e}")
            return
    except Exception as e:
        print(f"Error al seleccionar la previsión: {e}")
        return
    
    paciente=Paciente(rut,nombre,edad,prevision, departamento_general)
    pacientes.append(paciente)
    print("Paciente agregado exitosamente.")
    print(f"Total de pacientes registrados: {len(pacientes)}")

def buscar_paciente()->Paciente:
    rut=input("Ingrese rut del paciente: ")
    for p in pacientes:
        if p.rut==rut:
            return p
    print("Paciente no encontrado.")
    return None

def imprimir_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        print(paciente)
    else:
        print("No se encontró el paciente.")

def eliminar_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        pacientes.remove(paciente)
        print("El paciente ha sido eliminado correctamente.")
    else:
        print("No se encontró al paciente.")


def editar_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        print(paciente)
        print("1.- Editar nombre.")
        print("2.- Editar edad.")
        print("3.- Editar previsión.")
        print("0.- Salir.")
        op=leer_numero("Ingrese una opción: ")
        if op==1:
            nombre_nuevo=input("Ingrese nuevo nombre: ")
            try:
                paciente.nombre=nombre_nuevo
                print("El nombre del paciente ha sido actualizado correctamente.")
            except (TypeError, ValueError) as e:
                print(f"Error al actualizar el nombre del paciente: {e}")
        elif op==2:
            edad_nueva=leer_numero("Ingrese edad nueva: ")
            try:
                paciente.edad=edad_nueva
                print("La edad del paciente ha sido actualizada correctamente.")
            except (TypeError, ValueError) as e:
                print(f"Error al actualizar la edad del paciente: {e}")
        elif op==3:
            print("Tipos de previsión: ")
            print("1.- Fonasa")
            print("2.- Isapre")
            print("4.- Otro")
            op=leer_numero("Seleccione una previsión: ")
            try:
                if op==1:
                    paciente.prevision="Fonasa"
                    print("Previsión actualizada")
                elif op==2:
                    paciente.prevision="Isapre"
                    print("Previsión actualizada")
                elif op==3:
                    paciente.prevision="Particular"
                    print("Previsión actualizada")
                elif op==4:
                    paciente.prevision="Otro"
                    print("Previsión actualizada")
            except (TypeError, ValueError) as e:
                print(f"Error al actualizar la previsión del paciente: {e}")
    else:
        print("No se encotró al paciente.")

    
def main():
    while True:
        opcion=menu()
        if opcion==1:
            agregar_paciente()
        elif opcion==2:
            print("Editar paciente")
            editar_paciente()
        elif opcion==3:
            print("Eliminar un paciente")
            eliminar_paciente()
        elif opcion==4:
            print("Mostrar un paciente")
            imprimir_paciente()
        elif opcion==5:
            print("Mostrar todos los pacientes")
            imprimir_pacientes()
        elif opcion==0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.")





if __name__=="__main__":
    main()
