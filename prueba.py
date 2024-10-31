from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db_config = {
    'user': 'root',             # usuario de MySQL
    'password': '',             # contraseña de MySQL
    'host': 'localhost',        # host de MySQL
    'database': 'civicapp_db'   # reemplaza con el nombre de tu base de datos
}

# Conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Ruta para insertar un usuario
@app.route('/usuario', methods=['POST'])
def crear_usuario():
    datos = request.json
    query = '''
        INSERT INTO Usuario (Apellido_Paterno, Apellido_Materno, Nombre, Correo_electronico, RFC, Numero_celular, 
        Domicilio, Contraseña, CURP, Fecha_registro)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    valores = (
        datos['Apellido_Paterno'],
        datos['Apellido_Materno'],
        datos['Nombre'],
        datos['Correo_electronico'],
        datos['RFC'],
        datos['Numero_celular'],
        datos['Domicilio'],
        datos['Contraseña'],
        datos['CURP'],
        datos['Fecha_registro']
    )
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, valores)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Usuario creado con éxito'}), 201

# Ruta para obtener un usuario por ID
@app.route('/usuario/<int:id_usuario>', methods=['GET'])
def obtener_usuario(id_usuario):
    query = 'SELECT * FROM Usuario WHERE ID_usuario = %s'
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, (id_usuario,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(usuario) if usuario else jsonify({'message': 'Usuario no encontrado'}), 404

# Ruta para insertar una propuesta


@app.route('/propuesta', methods=['POST'])
def crear_propuesta():
    datos = request.json
    query = '''
        INSERT INTO Propuesta (ID_usuario, Nombre, Descripcion, Numero_votos, Fecha_creacion, Categoria, Ubicacion)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    valores = (
        datos['ID_usuario'],
        datos['Nombre'],
        datos['Descripcion'],
        datos['Numero_votos'],
        datos['Fecha_creacion'],
        datos['Categoria'],
        datos['Ubicacion']
    )
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, valores)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Propuesta creada con éxito'}), 201


# Ruta para obtener todas las propuestas
@app.route('/propuestas', methods=['GET'])
def obtener_propuestas():
    query = 'SELECT * FROM Propuesta'
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    propuestas = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(propuestas)



# Ruta para insertar un voto
@app.route('/voto', methods=['POST'])
def crear_voto():
    datos = request.json
    query = '''
        INSERT INTO Voto (ID_usuario, ID_propuesta, Fecha_voto)
        VALUES (%s, %s, %s)
    '''
    valores = (
        datos['ID_usuario'],
        datos['ID_propuesta'],
        datos['Fecha_voto']
    )
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, valores)
        conn.commit()
        result = {'message': 'Voto registrado con éxito'}
        status_code = 201
    except mysql.connector.IntegrityError:
        result = {'message': 'Este usuario ya ha votado por esta propuesta'}
        status_code = 409
    cursor.close()
    conn.close()
    return jsonify(result), status_code



# Ruta para obtener todos los votos de un usuario
@app.route('/usuario/<int:id_usuario>/votos', methods=['GET'])
def obtener_votos_usuario(id_usuario):
    query = '''
        SELECT * FROM Voto
        WHERE ID_usuario = %s
    '''
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, (id_usuario,))
    votos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(votos)

if __name__ == '__main__':
    app.run(debug=True)
