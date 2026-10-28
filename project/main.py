"""Punto de entrada de la aplicación FastAPI."""

from fastapi import FastAPI

from api.controller import router

app = FastAPI()
app.include_router(router)
