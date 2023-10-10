class LadoOscuro:
  def init(self, nombre, colorS, nave):
        self.nombre = nombre
        self.colorS = colorS
        self.nave = nave

    def mostrar(self):
        print(f"El sith {self.nombre} tiene el sable de color {self.colorS} y su nave es {self.nave}")
