class Producto:
    """Modelo que representa un producto en el sistema."""
    
    def __init__(self, id, nombre, precio, stock=0):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def to_dict(self):
        """Convierte el objeto a diccionario."""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'stock': self.stock
        }
    
    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento al precio."""
        self.precio = self.precio * (1 - porcentaje / 100)
        return self.precio