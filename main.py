from DB.conection import DAO
import funciones


def menu_principal():
    continuar = True
    while(continuar):
        opcion_correcta = False
        while(not opcion_correcta):
            print('+============== MENU PRINCIPAL ==============+')
            print('1.= Listar cursos')
            print('2.= Registrar cursos')
            print('3.= Actualizar cursos')
            print('4.= Eliminar cursos')
            print('5.= Salir')
            print('+============================================+')
            opcion = int(input('Seleccione un opcion: '))

            if opcion < 1 or opcion > 5:
                print('Opcion incorrecta, ingrese nuevamente...')
            elif opcion == 5:
                continuar = False
                print('Gracias por usar este sistema!!!')
                break
            else:
                opcion_correcta = True
                ejecutar_opcion(opcion)

 
def ejecutar_opcion(opcion):
    dao = DAO()

    # LISTAR CURSOS
    if opcion == 1:
        try:
            cursos = dao.listar_cursos()
            if len(cursos) > 0:
                funciones.listar_cursos(cursos)
            else:
                print('No se encontraron cursos...\n')
        except:
            print('Ocurrio un error...')

    # REGISTRAR CURSO
    elif opcion == 2:
        curso = funciones.pedir_datos()
        try:
            dao.registrar_curso(curso)
        except:
            print('Ocurrio un error...')

    # ACTUALIZAR CURSO
    elif opcion == 3:
        try:
            cursos = dao.listar_cursos()
            if len(cursos) > 0:
                curso = funciones.pedir_datos_actualizacion(cursos)
                if curso:
                    dao.actualizar_curso(curso)
                else:
                    print('Codigo de curso a actualizar no encontrado...\n')
            else:
                print('No se encontraron cursos...\n')
        except:
            print('Ocurrio un error...')

    # ELIMINAR CURSO
    elif opcion == 4:
        try:
            cursos = dao.listar_cursos()
            if len(cursos) > 0:
                codigo_eliminar = funciones.pedir_datos_eliminacion(cursos)
                if not(codigo_eliminar == ''):
                    dao.eliminar_curso(codigo_eliminar)
                else:
                    print('Codigo de curso no encontrado...\n')
            else:
                print('No se encontraron cursos...\n')
        except:
            print('Ocurrio un error...')

    else:
        print('Opcion no valida...')


menu_principal()
