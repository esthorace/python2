from main import validar_entero


def test_validar_entero__entero_positivo():
    assert validar_entero(23) == True


def test_validar_entero__cadena_valida():
    assert validar_entero("23") == True
    assert validar_entero("") == False


def test_validar_entero__cadena_valida_y_signo():
    assert validar_entero("+1") == True
    assert validar_entero("-1") == True


def test_validar_entero__estructura_invalida():
    assert validar_entero([1, 2]) == False


def test_validar_entero__bool():
    assert validar_entero(True) == False
