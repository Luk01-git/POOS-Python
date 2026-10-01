class Departamento:
	def __init__(self, id_departamento: int, prsd: str, nombre: str):
		self.id_departamento = id_departamento
		self.prsd = prsd
		self.nombre = nombre

	@property
	def id_departamento(self) -> int:
		return self._id_departamento

	@id_departamento.setter
	def id_departamento(self, id_departamento: int) -> None:
		self._id_departamento = id_departamento

	@property
	def prsd(self) -> str:
		return self._prsd

	@prsd.setter
	def prsd(self, prsd: str) -> None:
		self._prsd = prsd

	@property
	def nombre(self) -> str:
		return self._nombre

	@nombre.setter
	def nombre(self, nombre: str) -> None:
		self._nombre = nombre

	def __str__(self) -> str:
		return f"Departamento {self.id_departamento}: {self.nombre} (PRSD: {self.prsd})"

	def __repr__(self) -> str:
		return f"Departamento(id_departamento={self.id_departamento}, prsd='{self.prsd}', nombre='{self.nombre}')"
