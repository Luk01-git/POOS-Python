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
        if not isinstance(rut, str) or not rut.strip():
            raise TypeError("El RUT no puede estar vacío.")
        self._rut = rut.strip()

    @property
    def nombre(self)-> str:
        return self._nombre

    @nombre.setter
    def nombre(self,nombre:str)-> None:
        if not isinstance(nombre, str) or len(nombre.strip()) < 2:
            raise TypeError("El nombre no puede estar vacío y debe tener al menos 2 caracteres.")
        self._nombre = nombre.strip()

    @property
    def edad(self)->int:
        return self._edad

    @edad.setter
    def edad(self,edad:int)-> None:
        if not isinstance(edad, int) or edad < 0 or edad > 120:
            raise TypeError("Ingrese un numero valido (entero positivo).")
        self._edad=edad

    @property
    def prevision(self)->str:
        return self._prevision

    @prevision.setter
    def prevision(self, prevision:str)-> None:
        if not isinstance(prevision, str):
            raise TypeError("La previsión debe ser una cadena de texto.")
        prevision_l = prevision.strip()
        if prevision_l not in self.PREVISIONES_VALIDAS:
            opciones = ", ".join(self.PREVISIONES_VALIDAS)
            raise ValueError(f"La previsión debe ser una de las siguientes: {opciones}")
        self._prevision=prevision_l

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
