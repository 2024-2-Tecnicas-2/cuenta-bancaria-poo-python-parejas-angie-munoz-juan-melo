from cuenta_bancaria import CuentaBancaria


if __name__ == "__main__":
    cuenta = CuentaBancaria("Sam", "278391271", 1500.0)

    assert cuenta.get_titular() == "Sam"

    cuenta.set_titular("Lulu")
    assert cuenta.get_titular() == "Lulu"

    assert cuenta.get_numero_cuenta() == "278391271"

    assert cuenta.get_saldo() == 1500.0

    cuenta.ingresar(200.0)
    assert cuenta.get_saldo() == 1700.0

    cuenta.ingresar(-200.0)
    assert cuenta.get_saldo() == 1700.0

    cuenta.retirar(600.0)
    assert cuenta.get_saldo() == 1100.0

    cuenta.retirar(2000.0)
    assert cuenta.get_saldo() == 1100.0

    assert cuenta.calcular_interes() == 1116.5

    cuenta.set_tipo_interes(5.0)
    assert cuenta.calcular_interes() == 1155.0

    cuenta.set_tipo_interes(-2.0)
    assert cuenta.calcular_interes() == 1100.0  

    cuenta.set_tipo_interes(12.0)
    assert cuenta.calcular_interes() == 1100.0 

    print("Todas las pruebas pasaron correctamente.")