class Utilidades:
    def texto(self, string):
        # Verifica longitud mínima
        if len(string) < 3:
            return False
        # Verifica que no tenga espacios
        if ' ' in string:
            return False
        # Verifica que solo tenga letras (sin números ni símbolos)
        for c in string:
            if not (('a' <= c <= 'z') or ('A' <= c <= 'Z')):
                return False
        return True

    def documento(self, string):
        # Verifica longitud entre 3 y 15
        if len(string) < 3 or len(string) > 15:
            return False
        if ' ' in string:
            return False
        # Verifica que solo tenga dígitos
        for c in string:
            if not ('0' <= c <= '9'):
                return False
        return True
    
    def correo(self, string):
        # Verifica que no tenga espacios
        if ' ' in string:
            return False
        # Verifica que contenga un solo '@'
        if string.count('@') != 1:
            return False
        # Verifica que termine con '.com'
        if not string.endswith('.com'):
            return False
        # Verifica que '@' no esté al principio ni al final
        at_index = string.index('@')
        if at_index == 0 or at_index == len(string) - 1:
            return False
        # Verifica que haya algo entre '@' y '.com'
        if at_index + 1 == len(string) - 4:
            return False
        return True

    def num(self, string):
        # Verifica que el string no esté vacío
        if len(string) == 0:
            return False
        # Verifica que todos los caracteres sean dígitos
        for c in string:
            if not ('0' <= c <= '9'):
                return False
        # Convierte a entero
        valor = int(string)
        # No permite negativos
        if valor < 0:
            return False
        return valor