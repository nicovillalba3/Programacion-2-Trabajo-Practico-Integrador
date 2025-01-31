from Estudiante import * 
from Profesor import *
from Usuario import *
from Curso import *
from datos import *
from funciones_alumnos import *
from funciones_profesores import *
from Archivo import *

#-----------------FUNCIONES ALUMNOS-----------------------------------------------------------------------------------#

def ingresar_como_alumno(usuario):# tomo como parametro el Objeto Estudiante     
    
    while True:
        print("\nSubmenú de Alumno:")
        print("1. Matricularse a un curso")
        print("2. Desmatricularse a un curso")
        print("3. Ver curso")
        print("4. Volver al menú principal")
        print("Cursos del usuario:")
        for curso in usuario.cursos:
            print(curso.nombre)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            matricular_a_curso(usuario)
        elif opcion == "2":
           desmatricular_de_curso(usuario)
        elif opcion == "3":
            mostrar_cursos(usuario)
        elif opcion == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")     

def matricular_a_curso(usuario):

    
    cursos_disponibles = cursos 

    print("Cursos disponibles:")
    for i, curso in enumerate(cursos_disponibles, 1): #Enumerate es un método , crea una tupla para cada elemento, con el índice y el nombre.
        print(f"{i} {curso.nombre} - {curso.carrera.nombre} ") # Muestra el índice y el nombre



    while True:
        cursoIngresado = input("Ingrese el número del curso al que desea matricularse: ")
        if cursoIngresado.isdigit(): # isDigit retorna true en caso de que sea numero y en caso de que sea string devuelve false.
            cursoIngresado = int(cursoIngresado)
            if 1 <= cursoIngresado <= len(cursos_disponibles): # valida que el numero que ingrese el usuario este entre el 1 y el último num de curso.
                curso_seleccionado = cursos_disponibles[cursoIngresado - 1]
                
                if curso_seleccionado.nombre in usuario.cursos:
                    # El usuario ya se matriculo en ese curso
                    print(f"Ya estás matriculado en {curso_seleccionado.nombre}.")
                else:
                    # El usuario no está matriculado en el curso
                    if usuario.carrera == curso_seleccionado.carrera.nombre: #=> Se valida que la carrera del usuario y la carrera a la que pertenece el curso coincidan
                        print(f"No estás matriculado en {curso_seleccionado.nombre}.")
                        contra_user = input(f"Ingrese contraseña para matricularse a {curso_seleccionado.nombre} : ")     
                        
                        if contra_user == curso_seleccionado.contrasenia_matriculacion:
                            #usuario.matricular_en_curso(curso_seleccionado.nombre)
                            usuario.matricular_en_curso(curso_seleccionado)# => Método para matricular el usuario a un curso
                             
                            print("Se ha registrado correctamente su matriculación")
                        else:
                            print("Contraseña incorrecta")
                    else: # => Si la carrera del usuario y la carrera del curso no coinciden se muestra msj de error
                        print(f"No se puede inscribir a ese curso porque no pertenece a: {usuario.carrera}")

                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

def desmatricular_de_curso(usuario):

    if not usuario.cursos:
        print("No estás matriculado en ningún curso.")
        return  # Salir de la función si no está matriculado en ningún curso
    print("Cursos en los que estás matriculado:")
    for i, curso in enumerate(usuario.cursos, 1):
        print(f"{i}. {curso.nombre}")
    while True:
        cursoIngresado = input("Ingrese el número del curso del que desea desmatricularse: ")
        if cursoIngresado.isdigit():
            cursoIngresado = int(cursoIngresado)
            if 1 <= cursoIngresado <= len(usuario.cursos):
                curso_seleccionado = usuario.cursos[cursoIngresado - 1]
                usuario.desmatricular_de_curso(curso_seleccionado) # => Se llama al método del objeto Estudiante para desmatricularse de curso.
                print(f"Te has desmatriculado de {curso_seleccionado.nombre}.")                
                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")


def mostrar_archivos_de_curso(curso):
    # Verificar si el curso tiene archivos
    arrayArchivos = curso.archivos
    archivos_ordenados = sorted(arrayArchivos, key=lambda archivo: archivo.fecha)
    if arrayArchivos: #=> 
        print("Archivos del curso:")
        for archivo in archivos_ordenados:
            if hasattr(archivo, 'formato'):
                print(f"Nombre del archivo: {archivo.nombre}, Formato: {archivo.formato} , Fecha: {archivo.fecha}")
            else:
                print(f"El objeto {archivo} no tiene un atributo 'formato'.")
    else:
        print("El curso no tiene archivos.")


def mostrar_cursos(usuario):
    cursos_matriculados = usuario.cursos #=> En cursos_matriculados se guardan los cursos en los que el usuario se matriculó

    if not cursos_matriculados:
        print("No estás matriculado en ningún curso.")
    else:
        print("Cursos en los que estás matriculado:")
        for i, curso in enumerate(cursos_matriculados, 1): #=> Se enumeran los cursos
            print(f"{i}. {curso.nombre}")

        while True:
            curso_info = input("Ingrese el número del curso al que desea ver (0 para salir): ")
            if curso_info.isdigit(): #=> isDigit es un método que retorna true si el valor (en este caso curso_info) es número
                curso_seleccionado = int(curso_info)
                if 1 <= curso_seleccionado <= len(cursos_matriculados):
                    curso = cursos_matriculados[curso_seleccionado - 1] #=> en curso se guarda el curso seleccionado. Tomando el indice curso_seleccionado -1
                    print(f"Nombre: {curso.nombre}")
                    mostrar_archivos_de_curso(curso)  #=> Funcion que muestra los archivos 
                elif curso_seleccionado == 0:
                    break
                else:
                    print("Opción no válida. Por favor, ingrese un número válido o 0 para salir.")
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")


   

#----------------FIN FUNCIONES ALUMNOS-----------------------------------------------------------------------------------#
