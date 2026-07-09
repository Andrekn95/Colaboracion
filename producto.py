class Producto:

    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def mostrar_detalle(self):
        return f'Producto: {self.nombre} - {self.precio}'
