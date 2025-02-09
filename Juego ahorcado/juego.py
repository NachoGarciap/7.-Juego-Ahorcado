import random


class juegoAhorcado:

    def __init__(self):
        self.contador_intentos = 6
        self.palabras = ['h', 'pe', 'cuc', 'pito']
        self.palabras_animales = ['leon', 'hipopotamo', 'tigre', 'mono', 'perro']
        self.palabras_muebles = ['silla', 'mesa', 'estanteria', 'cama', 'lampara']
        self.palabras_colores = ['negro', 'blanco', 'azul', 'amarillo', 'verde']
        self.letras_usadas = []  # Para guardar las letras que ya se han usado
        self.palabra_oculta = []
        self.palabra_aleatoria = ''


        print("----- Bienvenido al juego del Ahorcado! -----")

    def menu_juego(self):
        while True:
            print('Categorias:')
            print('----------------------')
            print('|1. Animales(nivel 1)|')
            print('|2. Muebles (nivel 2)|')
            print('|3. Colores (nivel 3)|')
            print('----------------------')

            try:
                opcion = int(input("Elige un nivel para empezar a jugar: "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue

            if opcion == 1:
                self.seleccionar_categoria(self.palabras_animales)
                break
            elif opcion == 2:
                self.seleccionar_categoria(self.palabras_muebles)
                break
            elif opcion == 3:
                self.seleccionar_categoria(self.palabras_colores)
                break
            elif opcion == 4:
                print('Saliendo del juego...')
                break
            else:
                print('Introduce una categoria valida')

    def seleccionar_categoria(self, lista_palabras):
        self.palabra_aleatoria = random.choice(lista_palabras)
        self.palabra_oculta = ['_'] * len(self.palabra_aleatoria)  # Representar la palabra oculta con guiones bajos
        self.ejecutar_juego()

    def ejecutar_juego(self):
        while self.contador_intentos > 0 and '_' in self.palabra_oculta:
            print('--------------------')
            print("Palabra a adivinar: " + " ".join(self.palabra_oculta))  # unimos los elementos de la lista
            print(f"Letras ya usadas: {', '.join(self.letras_usadas)}")

            letra_usuario = input('Introduce una letra: ')

            if len(letra_usuario) != 1:
                print('Por favor, introduce solo una letra!')
                continue  # Si el usuario ingresa más de una letra, vuelve al inicio

            if letra_usuario in self.letras_usadas:
                print("Ya has usado esa letra. Intenta con otra.")
                continue  # Vuelve al inicio del bucle si ya se usó la letra

            self.letras_usadas.append(letra_usuario)  # Añadir la letra a la lista de letras usadas

            if letra_usuario in self.palabra_aleatoria:
                print('la letra esta en la palabra')
                for i in range(len(self.palabra_aleatoria)):
                    if self.palabra_aleatoria[i] == letra_usuario:
                        self.palabra_oculta[i] = letra_usuario

                print(" ".join(self.palabra_oculta))

            else:
                self.contador_intentos -= 1
                print('Letra incorrecta')
                print(f'Te quedan {self.contador_intentos} intentos!')

            if '_' not in self.palabra_oculta:
                print(f'Has ganado!La palabra aleatoria es: {self.palabra_aleatoria}')

        else:
            if self.contador_intentos == 0:
                print(f'Has perdido!, la palabra aleatoria era: {self.palabra_aleatoria}')



