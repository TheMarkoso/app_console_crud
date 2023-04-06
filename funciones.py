
def listar_cursos(cursos):
    print('\nCursos: \n')
    contador = 1 
    for cur in cursos:
        datos = "{0}. Codigo: {1} | Nombre: {2} ({3} creditos)"
        #print(f'contado. Codigo: {cur[0]} | Nombre: {cur[1]} ({cur[2]} creditos)')
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador += 1
    print(' ')


def pedir_datos():
    codigo_correcto = False
    while(not codigo_correcto):
        codigo = input('Ingrese codigo: ')
        if len(codigo) == 6:
            codigo_correcto = True
        else:
            print('Codigo incorrecto: Debe tener 6 digitos.')

    nombre = input('Ingrese nombre: ')

    creditos_correcto = False
    while(not creditos_correcto):
        creditos = input('Ingrese creditos: ')
        if creditos.isnumeric():
            if int(creditos) > 0:
                creditos_correcto = True
                creditos = int(creditos)
            else:
                print('Los creditos deben ser mayor a 0.')
        else:
            print('Creditos incorrecto: Debe ser un numero unicamente.')

    curso = (codigo, nombre, creditos)
    return curso


def pedir_datos_actualizacion(cursos):
    listar_cursos(cursos)

    existe_codigo = False
    codigo_editar = input('Ingrese el codigo del curso a editar: ')
    for cur in cursos:
        if cur[0] == codigo_editar:
            existe_codigo = True
            break
    
    if existe_codigo:
        nombre = input('Ingrese nombre a modificar: ')

        creditos_correcto = False
        while(not creditos_correcto):
            creditos = input('Ingrese creditos a modificar: ')
            if creditos.isnumeric():
                if int(creditos) > 0:
                    creditos_correcto = True
                    creditos = int(creditos)
                else:
                    print('Los creditos deben ser mayor a 0.')
            else:
                print('Creditos incorrecto: Debe ser un numero unicamente.')

        curso = (codigo_editar, nombre, creditos)

    else:
        curso = None

    return curso



def pedir_datos_eliminacion(cursos):
    listar_cursos(cursos)
    
    existe_codigo = False
    codigo_eliminar = input('Ingrese el codigo del curso a eliminar: ')
    for cur in cursos:
        if cur[0] == codigo_eliminar:
            existe_codigo = True
            break

    if not existe_codigo:
        codigo_eliminar = ''

    return codigo_eliminar
