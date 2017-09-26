class Cola(object):
	def__init__(self):
		self.items[]
	def encolar(self,x):
		self.items.append(x)
	
	def esta_vacia(self):
		if len(self.items)==0:
			return True
		else
			return False

	def desencolar(self):
		if self.esta_vacia():
			return None 
		else:
			return self.items.pop(0)
c1=Cola()
c1.encolar("carro 1")
c1.encolar("carro 2")
c1.encolar("carro 3")
print(c1.esta_vacia)
print(c1.desencolar())
print(c1.desencolar())
print(c1.desencolar())
print(c1.esta_vacia)