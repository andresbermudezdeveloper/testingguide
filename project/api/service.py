"""Capa de negocio: contiene la lógica y las reglas de la API."""

def return_sum(a: int, b: int) -> int:
    """Suma dos números enteros y devuelve el resultado."""

    # Validar que ambos parámetros sean números enteros;
    # cualquier otro tipo (float, str, etc.) lanza TypeError
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Solo se permiten números enteros")

    # Retornar el resultado de la suma de los 2 numeros
    return a + b
