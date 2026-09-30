from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
        
        def __init__(self, data):
            self.id = data.get('id')
            self.nombre = data.get('nombre')
            self.email = data.get('email')
            self.password = data.get('password')
            self.created_at = data.get('created_at')
            self.updated_at = data.get('updated_at')


        @classmethod
        def save(cls, data):
            query = "INSERT INTO usuarios (nombre, email, password) VALUES (%(nombre)s, %(email)s, %(password)s);"
            result = connectToMySQL('esquema_canciones').query_db(query, data)
            return result

        @classmethod
        def get_all(cls):
            query = "SELECT * FROM usuarios;"
            results = connectToMySQL('esquema_canciones').query_db(query)
            usuarios = []
            for row in results:
                usuarios.append(cls(row))
            return usuarios

        @classmethod
        def get_by_id(cls, id):
            query = "SELECT * FROM usuarios WHERE id = %(id)s;"
            data = {'id': id}
            result = connectToMySQL('esquema_canciones').query_db(query, data)
            if result:
                return cls(result[0])
            else:
                return None
        @classmethod
        def get_favoritos(cls, usuario_id):
            query = "SELECT * FROM favoritos WHERE usuario_id = %(usuario_id)s;"
            data = {'usuario_id': usuario_id}
            results = connectToMySQL('esquema_canciones').query_db(query, data)
            favoritos = []
            for row in results:
                favoritos.append(row)
            return favoritos