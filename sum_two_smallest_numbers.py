def sum_two_smallest_numbers(numbers):
    numeroMenor = obtenerMenorNumeroArray(numbers)
    indice = numbers.index(numeroMenor)
    numbers.pop(indice)
    numeroMenor1 = obtenerMenorNumeroArray(numbers)
    
    sol = numeroMenor1 + numeroMenor
   
    return sol    
    
    
    
def obtenerMenorNumeroArray(numeros):
    mayor = numeros[0]
    for elemento in numeros:
        if elemento < mayor:
            mayor = elemento
    return mayor

