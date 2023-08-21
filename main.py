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
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo= modelo
        self.precio=precio
        Asiento.asientos= asientos
        self.marca = marca
        Motor.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        numAsientos = 0
        for i in range(len(self.asientos)):
            if self.asientos[i] != None:
                numAsientos +=1
        return numAsientos
    
    def verificarIntegridad(self):
        if self.motor.registro == self.registro:
            for i in range(len(self.asientos)):
                if self.asientos[i] != None:
                    if self.asientos[i].registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"






