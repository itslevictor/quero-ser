def menor_distancia(array1, array2):
    # Inicializa a menor distância com a diferença absoluta do primeiro elemento de cada array
    menor_dist = abs(array1[0] - array2[0])
    
    # Percorre cada elemento do primeiro array
    for num1 in array1:
        # Percorre cada elemento do segundo array
        for num2 in array2:
            # Calcula a diferença absoluta entre os dois números
            dist = abs(num1 - num2)
            # Se a distância calculada for menor que a menor distância atual, atualiza a menor distância
            if dist < menor_dist:
                menor_dist = dist
    
    return menor_dist

# Exemplo de uso da função
array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array2 = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

print(menor_distancia(array1, array2))  #: 5
