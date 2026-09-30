from config.mysqlconnection import connectToMySQL

class Favorito:

    def __init__(self, data):
        self.usuario_id = data.get('usuario_id')
        self.cancion_id = data.get('cancion_id')

    