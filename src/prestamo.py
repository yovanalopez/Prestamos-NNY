from datetime import datetime

class Prestamo:
    def __init__ (self, ID, amigo, objeto, fecha):
        self.__ID = ID
        self.__amigo = amigo
        self.__objeto = objeto
        self.__fecha = fecha
        self.__vencido = False # False = no vencido, True = vencido

    def get_ID(self):
        return self.__ID
    def get_amigo(self):
        return self.__amigo
    def get_objeto(self):
        return self.__objeto
    def get_fecha(self):
        return self.__fecha
    def get_vencido(self):
        return self.__vencido
    def set_vencido(self, estado):
        self.__vencido = estado

    def calcular_dias_restantes(self):
        fecha_actual = datetime.now().date()
        return (self.__fecha - fecha_actual).days

    def info(self):
        return f"Amigo: {self.__amigo.info()} | Objeto: {self.__objeto.info()} | Vence el: {self.__fecha.strftime('%d/%m/%Y')}"