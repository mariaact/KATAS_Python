def domain_name(url):
    palabras = url.split(sep='.')
    cont = 0
    sol = ''
    
    for x in palabras:
                        
        if(x.startswith('co')):
            sol = palabra 
        elif('www' in x):
            sol = palabras[cont+1]
        elif(x.startswith('https://')):
            palabras1 = x.split(sep='/')  
            sol = palabras1[-1]
        elif(len(palabras) == 2):
            sol = palabras[0]
        elif(len(palabras) == 1):
            sol = palabras[0]
        elif('html' in x):
            if not bool(sol):
                sol = palabras[0]        
        elif('php' in x):
            if(len(sol) ==0):
                sol = palabras[0]
        elif('jp' in x):            
            if(len(sol) == 0):
                sol = palabras[0]
            
        palabra = x
        cont = cont +1

    if('/' in sol):
        palabras1 = sol.split(sep='/')    
        sol = palabras1[-1]
    
    return sol

domain_name('j6pi5nmtgrkcik9lmg8.pro/default.html')