class MaximoComunDivisor:
    def __init__(self, numeros=None):
        if numeros is None:
            numeros = []
        self._numeros = numeros

    @property
    def numeros(self):
        """Getter para la lista de números"""
        return self._numeros

    @numeros.setter
    def numeros(self, nueva_lista):
        """Setter para la lista de números"""
        if not all(isinstance(num, int) for num in nueva_lista):
            raise ValueError("Todos los elementos deben ser enteros")
        self._numeros = nueva_lista

    def calcularMCD(self):
        """Calcula el MCD de todos los números en la lista"""
        if not self._numeros:
            return 0

        def mcd_de_dos(a, b):
            while b:
                a, b = b, a % b
            return a

        resultado = self._numeros[0]
        for num in self._numeros[1:]:
            resultado = mcd_de_dos(resultado, num)
            if resultado == 1:
                break  # El MCD no puede ser menor que 1
        return resultado


if __name__ == '__main__':
    # Entrada de datos
    cantidadNumeros = int(input("Cantidad de números: "))
    numeros = []
    for i in range(cantidadNumeros):
        print(f"Número {i + 1:2}: ", end="", flush=True)
        numeros.append(int(input("")))

    print(f"Números = {numeros}")

    # Creación del objeto y cálculo
    operacionesEnteros = MaximoComunDivisor(numeros)
    print(f"MCD = {operacionesEnteros.calcularMCD()}")
