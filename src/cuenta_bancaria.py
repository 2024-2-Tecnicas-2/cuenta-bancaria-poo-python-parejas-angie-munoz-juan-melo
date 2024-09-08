class CuentaBancaria:
    # TODO: Aquí va el código de la clase CuentaBancaria

    def __init__(self, titular, numero_cuenta, saldo):
        self.__titular = titular
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.__tipo_interes = 1.5

    # Métodos getter y setter
    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_saldo(self):
        return self.__saldo

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        if 0 <= cantidad <= self.__saldo:
            self.__saldo -= cantidad

    def calcular_interes(self):
        return self.__saldo * (1 + self.__tipo_interes / 100)

    def set_tipo_interes(self, tipo_interes):
        if 0 <= tipo_interes <= 10:
            self.__tipo_interes = tipo_interes