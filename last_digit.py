def last_digit(n1, n2):
    
    numero1 = n1
    numero2 = n2

    print(numero1)
    print(numero2)
    
    numero = pow(n1, n2)
    
    if(len(str(numero)) > 0):
        sol =  int(str(numero)[-1])
    else:
        sol = numero
        
    return sol


print(last_digit(10, 10 ** 10))

#last_digit(4, 1)                # returns 4
#last_digit(4, 2)                # returns 6
#last_digit(9, 7)                # returns 9
#last_digit(10, 10 ** 10)        # returns 0
#last_digit(2 ** 200, 2 ** 300)  # returns 6
