"""Tests unitarios de la capa service."""

import pytest

from api.service import return_sum


def test_return_sum_adds_two_positive_numbers():
    """Verifica que la función suma dos números positivos correctamente."""
    # Arrange: preparar los datos de entrada
    a = 2
    b = 3

    # Act: ejecutar la función que quiero probar
    result = return_sum(a, b)

    # Assert: comprobar que el resultado es el esperado
    assert result == 5


def test_return_sum_adds_two_negative_numbers():
    """Verifica que la función suma dos números negativos correctamente."""
    # Arrange: preparar los datos de entrada
    a = -2
    b = -3

    # Act: ejecutar la función que quiero probar
    result = return_sum(a, b)

    # Assert: comprobar que el resultado es el esperado
    assert result == -5


def test_return_sum_rejects_floats():
    """Verifica que la función rechaza números decimales con un TypeError."""
    # Arrange: preparar los datos de entrada
    a = 0.1
    b = 0.2

    # Act y Assert: ejecutar la función y comprobar que lanza el error esperado
    with pytest.raises(TypeError):
        return_sum(a, b)


@pytest.mark.parametrize("a, b", [(1, 0.5), (0.5, 1)])
def test_return_sum_rejects_mixed_floats(a, b):
    """Verifica que la función rechaza un decimal combinado con un entero."""
    # Act y Assert: ejecutar la función y comprobar que lanza el error esperado
    with pytest.raises(TypeError):
        return_sum(a, b)


def test_return_sum_rejects_strings():
    """Verifica que la función rechaza textos con un TypeError."""
    # Arrange: preparar los datos de entrada
    a = "a"
    b = "b"

    # Act y Assert: ejecutar la función y comprobar que lanza el error esperado
    with pytest.raises(TypeError):
        return_sum(a, b)
