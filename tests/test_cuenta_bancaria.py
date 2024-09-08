import sys
import os
import unittest

import cuenta_bancaria

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


class TestCalcular(unittest.TestCase):
    
    # TODO Adiciona tus pruebas unitarias aquí.
    cuenta = cuenta_bancaria("Sam", "278391271", 1500.0)

    assert cuenta.get_titular() == "Sam"

    cuenta.set_titular("Lulu")
    assert cuenta.get_titular() == "Lulu"

    assert cuenta.get_numero_cuenta() == "278391271"

    assert cuenta.get_saldo() == 1500.0

    cuenta.ingresar(200)
    assert cuenta.get_saldo == 1700.0

    cuenta.ingresar(-200)
    assert cuenta.get_saldo == 1700.0

    cuenta.retirar(600)
    assert cuenta.get_saldo() == 1100.0

    cuenta.retirar(2000)
    assert cuenta.get_saldo == 1100.0

    assert cuenta.calcular_interes() == 1116.5

    cuenta.set_tipo_interes(5,0)
    assert cuenta.calcular_interes() == 1155.0

    cuenta.set_tipo_interes(-2.0)
    assert cuenta.calcular_interes() == 1100.0

    cuenta.set_tipo_interes(12.0)
    assert cuenta.calcular_interes() == 1100.0

    print("Todas las pruebas fueron correctas")

    if __name__ == '__main__':
        unittest.main()