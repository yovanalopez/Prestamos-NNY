class Cliente:
    def __init__ (self, nombre, apellido, documento, correo, tpd):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__documento = documento
        self.__correo = correo
        self.__tpd = tpd

    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_documento(self):
        return self.__documento
    def get_correo(self):
        return self.__correo
    def get_tpd(self):
        return self.__tpd

    def info(self):
        return f"{self.__nombre} {self.__apellido} (Doc: {self.__documento})"