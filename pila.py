class Pila(object):
	def__init__(self):
		self.items[]
	def apilar(self,dato):
		self.items.append(dato)
	def desapilar(self):
		if self.esta_vacia():
			return None 
		else:
			return self.items.pop()
	def esta_vacia(self):
		if len(self.items)==0:
			return True
		else
			return False

p1=Pila()
p1.apilar("waffle 1")
p1.apilar("waffle 2")
p1.apilar("waffle 3")
print(p1.esta_vacia)
print(p1.desapilar())
print(p1.desapilar())
print(p1.desapilar())
print(p1.esta_vacia)