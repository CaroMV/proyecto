from config.mysqlconnection import connectToMySQL

class Cancion:

    def __init__(self, data):
        self.id = data.get('id')
        self.titulo = data.get('titulo')
        self.artista = data.get('artista')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    
    def save(self):
        query = "INSERT INTO canciones (titulo, artista) VALUES (%(titulo)s, %(artista)s);"
        result = connectToMySQL('esquema_canciones').query_db(query, self.__dict__)
        return result
    def get_all(cls):
        query = "SELECT * FROM canciones;"
        results = connectToMySQL('esquema_canciones').query_db(query)
        canciones = []
        for row in results:
            canciones.append(cls(row))
        return canciones

    def get_by_id(cls, id):
        query = "SELECT * FROM canciones WHERE id = %(id)s;"
        data = {'id': id}
        result = connectToMySQL('esquema_canciones').query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None

    def update(self):
        query = "UPDATE canciones SET titulo = %(titulo)s, artista = %(artista)s WHERE id = %(id)s;"
        result = connectToMySQL('esquema_canciones').query_db(query, self.__dict__)
        return result

    def delete(self):
        query = "DELETE FROM canciones WHERE id = %(id)s;"
        result = connectToMySQL('esquema_canciones').query_db(query, self.__dict__)
        return result
    