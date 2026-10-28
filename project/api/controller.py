"""Capa HTTP: recibe las peticiones y devuelve las respuestas."""

from fastapi import APIRouter

from api.service import return_sum

# Router del controlador; los endpoints se registran aquí con @router.get, @router.post, etc.
router = APIRouter()


@router.get("/sum")
def sum_numbers(a: int, b: int) -> dict[str, int]:
    """Suma dos números enteros recibidos como query params."""
    return {"result": return_sum(a, b)}
