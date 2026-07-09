class Cliente:
    """Modelo que representa un cliente en el sistema."""
    
    def __init__(self, id, nombre, email, telefono=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    
    def to_dict(self):
        """Convierte el objeto a diccionario."""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono
        }
    
    def es_email_valido(self):
        """Valida que el email tenga formato correcto."""
        return '@' in self.email and '.' in self.email