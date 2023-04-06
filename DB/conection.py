import mysql.connector
from mysql.connector import Error

# DATA ACCESS OBJECT
class DAO():

    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='', # nombre de usuario en mysql
                password='', # password de usuario mysql
                db='universidad'
            )
        except Error as ex:
            print('Error al intentar la conexion: {0}'.format(ex))

    def listar_cursos(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute('SELECT * FROM curso ORDER BY nombre ASC')
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print('Error al intentar la conexion: {0}'.format(ex))

    def registrar_curso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO curso (codigo, nombre, creditos) VALUES ('{0}', '{1}', '{2}')"
                cursor.execute(sql.format(curso[0], curso[1], curso[2]))
                self.conexion.commit()
                print('Curso registrado!!!')
            except Error as ex:
                print('Error al intentar la conexion: {0}'.format(ex))

    def actualizar_curso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE curso SET nombre = '{0}', creditos = '{1}' WHERE codigo = '{2}'"
                cursor.execute(sql.format(curso[1], curso[2], curso[0]))
                self.conexion.commit()
                print('Curso Actualizado!!!')
            except Error as ex:
                print('Error al intentar la conexion: {0}'.format(ex))




    def eliminar_curso(self, codigo_curso_eliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM curso WHERE codigo = '{0}'"
                cursor.execute(sql.format(codigo_curso_eliminar))
                self.conexion.commit()
                print('Curso Eliminado!!!')
            except Error as ex:
                print('Error al intentar la conexion: {0}'.format(ex))





