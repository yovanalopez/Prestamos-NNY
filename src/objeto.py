class Objeto:
    def __init__ (self, ID, nombre, precio, id_categoria = 0):
        self.__ID = ID
        self.__nombre = nombre
        self.__precio = precio
        self.__id_categoria  = id_categoria
        self.__estado = 0 # 0=Disponible, 1=Prestado, 2=Vendido

    def get_ID(self):
        return self.__ID
    def get_nombre(self):
        return self.__nombre
    def get_precio(self):
        return self.__precio
    def get_id_categoria(self):
        return self.__id_categoria
    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def info(self):
        categoria = ["Videojuegos" ,"Libros" ,"Música y video" ,"Herramientas" ,"Dinero" ,"Misceláneo y varios"][self.__id_categoria - 1]
        return f"{self.__nombre} (ID: {self.__ID}) - Precio: ${self.__precio} - Categoría: {categoria}"