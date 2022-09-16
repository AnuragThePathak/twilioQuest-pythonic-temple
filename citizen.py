class Citizen:
	"""My first python class"""
	greeting = "For the glory of Python!"
	
	def __init__(self, first_name, last_name) -> None:
		self.first_name = first_name
		self.last_name = last_name

	def full_name(self):
		return f"{self.first_name} {self.last_name}"