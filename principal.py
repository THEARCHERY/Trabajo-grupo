class Fuerza:
	def  ejecutar():
		nombre = input("introduce el nombre del personaje: ")
		Lado = input(F"¿{nombre} pertenece al lado (l)uminoso o (o)scuro de la fuerza? ")
		colorS = input("¿De que color es su sable?")
		nave = input ("¿Que nave usa ?")

		if Lado.lower() == "l":
			personaje = LadoLuminoso(nombre,colorS,nave)
		elif Lado.lower() == "o":
			personaje = LadoOscuro(nombre,colorS,nave)
		else:
			print("te has equivocado vuelve a intentar")
			return

			personaje.mostrar()

if __name__ == "__main__":
	Fuerza.ejecutar()

