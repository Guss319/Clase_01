# Definición de la clase Vehiculo
class Vehiculo:
    def __init__(self, pMarca, pModelo):
        self.marca = pMarca
        self.modelo = pModelo

    def ObtenerInformacion1(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# Definición de la clase Coche que hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def ObtenerInformacion2(self):
        return f"Auto:   {super().ObtenerInformacion1()}, Puertas: {self.puertas}"

# Definición de la clase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def ObtenerInformacion3(self):
        return f"Moto:   {super().ObtenerInformacion1()}, Cilindrada: {self.cilindrada}"

# Crear instancias de las clases Coche y Moto
miAuto = Auto("Chevrolet", "Cruze", 4)
miMoto = Moto("Yamaha", "R1", "1000cc")

# Obtener información de los vehículos
print(miAuto.ObtenerInformacion2())
print(miMoto.ObtenerInformacion3())
