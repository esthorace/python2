from abc import ABC, abstractmethod


class RepositorioUsuarios(ABC):
    @abstractmethod
    def leer_datos(self) -> list: ...

    @abstractmethod
    def escribir_datos(self, datos: list) -> None: ...

    @abstractmethod
    def agregar_datos(self, usuario: dict) -> None: ...
