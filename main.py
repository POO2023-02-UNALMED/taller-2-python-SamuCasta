class Asiento:
    def __init__(self,color,precio,registro):
        self.color= color
        self.precio=precio
        self.registro = registro

    def cambiarColor(self,color):
         if (color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco"):
            self.color=color

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self,registro):
        self.registro=registro
    
    def asignarTipo(self,tipo):
        if (tipo=="electrico" or tipo=="gasolina"):
            self.tipo=tipo

class Auto:
    cantidadCreados = cantidadCreados
    
