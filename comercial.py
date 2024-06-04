
class CentroComercial:

    def get_nombre_tienda(self):
        pass
    def get_tipo_comercio(self):
        pass
    def get_descuento(self):
        pass
    def calcular_descuento(self):
        pass
    def __str__(self):
        pass

class Tienda(CentroComercial):

    def __init__(self, nombre_tienda, tipo_comercio, descuento):
        self.nombre_tienda = nombre_tienda
        self.tipo_comercio = tipo_comercio
        self.descuento = descuento

    def get_nombre_tienda(self):
        return self.nombre_tienda
    def get_tipo_comercio(self):
        return self.tipo_comercio
    def get_descuento(self):
        return self.descuento
    def calcular_descuento(self):
        if self.tipo_comercio.lower() == "ropa de niño":
            return self.descuento * 0.8
        elif self.tipo_comercio.lower() == "dispositivos electrónicos":
            return self.descuento * 0.4
        else:
            return 0

    def __str__(self):
        return f"Nombre de la tienda: {self.nombre_tienda}\n" \
               f"Tipo de comercio: {self.tipo_comercio}\n" \
               f"Descuento aplicado: {self.calcular_descuento()}"

class CalcularDescuento:

    def __init__(self, tipo_comercio):
        self.tipo_comercio = tipo_comercio
    def calcular_descuento(self):
        pass

class RopaDeNinoDescuento(CalcularDescuento):

    def __init__(self, tipo_comercio):
        super().__init__(tipo_comercio)
    def calcular_descuento(self):
        return 0.8


class DispositivosElectronicosDescuento(CalcularDescuento):

    def __init__(self, tipo_comercio):
        super().__init__(tipo_comercio)

    def calcular_descuento(self):
        return 0.4

tienda1 = Tienda("Tienda Ropa Niño", "Ropa de Niño", 0.5)
tienda2 = Tienda("Tienda Electrónica", "Dispositivos Electrónicos", 0.7)

print(tienda1)
print(tienda2)

descuento_ropa_nino = CalcularDescuento("Ropa de Niño")
descuento_electronicos = CalcularDescuento("Dispositivos Electrónicos")

print(f"Descuento ropa de niño: {descuento_ropa_nino.calcular_descuento()}")
print(f"Descuento dispositivos electrónicos: {descuento_electronicos.calcular_descuento()}")
