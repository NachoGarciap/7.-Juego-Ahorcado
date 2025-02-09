import random

contador_intentos = 6

palabras = ['h', 'pe', 'cuc', 'pito']
letras_usadas = []  # Para guardar las letras que ya se han usado

palabra_aleatoria = random.choice(palabras)

palabra_oculta = ['_'] * len(palabra_aleatoria)  # Representar la palabra oculta con guiones bajos

print("----- Bienvenido al juego del Ahorcado! -----")

while contador_intentos > 0 and '_' in palabra_oculta:
    print("Palabra a adivinar: " + " ".join(palabra_oculta))  # unimos los elementos de la lista
    print(f"Letras ya usadas: {', '.join(letras_usadas)}")

    letra_usuario = input('Introduce una letra: ')
    if letra_usuario in letras_usadas:
        print("Ya has usado esa letra. Intenta con otra.")
        continue  # Vuelve al inicio del bucle si ya se usó la letra

    letras_usadas.append(letra_usuario)  # Añadir la letra a la lista de letras usadas

    if letra_usuario in palabra_aleatoria:
        print('la letra esta en la palabra')
        for i in range(len(palabra_aleatoria)):
            if palabra_aleatoria[i] == letra_usuario:
                palabra_oculta[i] = letra_usuario

        print(" ".join(palabra_oculta))

    else:
        contador_intentos -= 1
        print('Letra incorrecta')
        print(f'Te quedan {contador_intentos} intentos!')

    if '_' not in palabra_oculta:
        print(f'Has ganado!La palabra aleatoria es: {palabra_aleatoria}')

else:
    if contador_intentos == 0:
        print(f'Has perdido!, la palabra aleatoria era: {palabra_aleatoria}')

