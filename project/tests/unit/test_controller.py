"""Tests de la capa controller."""

import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_sum_returns_result_for_two_integers():
    """Verifica que GET /sum devuelve 200 y la suma de dos enteros."""
    # Arrange: preparar los parámetros de la petición
    params = {"a": 2, "b": 3}

    # Act: enviar la petición al endpoint
    response = client.get("/sum", params=params)

    # Assert: comprobar el código de estado y el cuerpo de la respuesta
    assert response.status_code == 200
    assert response.json() == {"result": 5}


@pytest.mark.parametrize(
    "a, b, invalid_params",
    [("x", "y", ["a", "b"]), ("x", 3, ["a"]), (3, "x", ["b"])],
)
def test_sum_rejects_string_param(a, b, invalid_params):
    """Verifica que GET /sum devuelve 422 cuando algún parámetro es texto."""
    # Arrange: preparar los parámetros, con texto en "a", en "b" o en ambos
    params = {"a": a, "b": b}

    # Act: enviar la petición al endpoint
    response = client.get("/sum", params=params)

    # Assert: comprobar el código de estado y que los errores señalan solo a los parámetros inválidos
    assert response.status_code == 422
    error_locs = [error["loc"] for error in response.json()["detail"]]
    assert error_locs == [["query", param] for param in invalid_params]


@pytest.mark.parametrize(
    "a, b, invalid_params",
    [(0.1, 0.2, ["a", "b"]), (0.5, 3, ["a"]), (3, 0.5, ["b"])],
)
def test_sum_rejects_float_param(a, b, invalid_params):
    """Verifica que GET /sum devuelve 422 cuando algún parámetro es decimal."""
    # Arrange: preparar los parámetros, con decimal en "a", en "b" o en ambos
    params = {"a": a, "b": b}

    # Act: enviar la petición al endpoint
    response = client.get("/sum", params=params)

    # Assert: comprobar el código de estado y que los errores señalan solo a los parámetros inválidos
    assert response.status_code == 422
    error_locs = [error["loc"] for error in response.json()["detail"]]
    assert error_locs == [["query", param] for param in invalid_params]
