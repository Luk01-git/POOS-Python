from departamento import Departamento


class Paciente:

    PREVISIONES_VALIDAS:set[str]={"Fonasa","Isapre","Particular","Otro"}

    def __init__(self, rut:str, nombre:str, edad:int, prevision:str, departamento: Departamento | None = None):
        self.rut = rut
        self.nombre=nombre
        self.edad=edad
        self.prevision=prevision
        self.departamento=departamento

    @property
    def rut(self)-> str:
        return self._rut

    @rut.setter
    def rut(self,rut:str)-> None:
        self._rut = rut

    @property
    def nombre(self)-> str:
        return self._nombre

    @nombre.setter
    def nombre(self,nombre:str)-> None:
        self._nombre = nombre

    @property
    def edad(self)->int:
        return self._edad

    @edad.setter
    def edad(self,edad:int)-> None:
        self._edad=edad

    @property
    def prevision(self)->str:
        return self._prevision

    @prevision.setter
    def prevision(self,prevision:str)-> None:
        self._prevision=prevision

    @property
    def departamento(self) -> Departamento | None:
        return self._departamento

    @departamento.setter
    def departamento(self, departamento: Departamento | None) -> None:
        self._departamento = departamento

    def __str__(self)-> str:
        detalle_departamento = str(self.departamento) if self.departamento else "Sin departamento asignado"
        return f"Información del paciente:\nRUT: {self.rut}\nNombre: {self.nombre}\nEdad: {self.edad}\nPrevisión: {self.prevision}\n{detalle_departamento}"

    def __repr__(self)-> str:
        return f"Paciente(rut='{self.rut}', nombre='{self.nombre}', edad={self.edad}, prevision='{self.prevision}', departamento={self.departamento!r})"
