import mysql.connector
from mysql.connector import Error

#funcion para ingresar datos con fecha
def insertar_datos_usuario(Apellido_Paterno,Apellido_Materno,Nombre, Correo_electronico, RFC, Numero_celular, Domicilio, Contraseña, CURP, Fecha_registro):
    try:
        # Conectar a la base de datos
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',  # Usuario predeterminado de XAMPP
            password='',  # Contraseña predeterminada en XAMPP suele estar vacía
            database='CivicApp_db'  # Cambia esto al nombre de tu base de datos
        )

        if conexion.is_connected():
            cursor = conexion.cursor()

            # SQL para insertar datos en una tabla, incluyendo la fecha de ingreso
            consulta = """
            INSERT INTO Usuario (Apellido_Paterno,Apellido_Materno,Nombre, Correo_electronico, RFC, Numero_celular, Domicilio, Contraseña, CURP, Fecha_registro)
            VALUES (%s, %s, %s, %s)
            """
            # Genera la fecha y hora actual
            fecha_actual = datetime.now()

            # Valores a insertar
            valores = (nombre, edad, ciudad, fecha_actual)

            cursor.execute(consulta, valores)  # Ejecuta la consulta con los valores dados
            conexion.commit()  # Confirma los cambios en la base de datos
            print("Datos insertados correctamente.")

    except Error as e:
        print(f"Error al conectar o insertar datos en MySQL: {e}")

    finally:
        # Cerrar la conexión a la base de datos
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión a MySQL cerrada.")
