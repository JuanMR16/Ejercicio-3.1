class ComparadorValores:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def comparar(self):
        '''Compara los dos valores y devuelve el resultado de la comparación.'''
        if self.valor1 > self.valor2:
            return f"El primer valor ({self.valor1}) es mayor que el segundo valor ({self.valor2})."
        elif self.valor2 > self.valor1:
            return f"El segundo valor ({self.valor2}) es mayor que el primer valor ({self.valor1})."
        else:
            return "Ambos valores son iguales."

print("Comparación de dos valores para determinar el mayor")

valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))

comparador = ComparadorValores(valor1, valor2)

resultado = comparador.comparar()
print(resultado)

print("Comparación completada.")