# --- Función para ingresar transiciones ---
def transitions():
    #instrucciones
    print("\nProcederá a escribir transiciones de la forma d(q,x)=(p,Y,L) en donde:")
    print(" - q: estado actual")
    print(" - x: símbolo actual")
    print(" - p: se pasa de estado 'q' a estado 'p'")
    print(" - Y: se cambia el símbolo 'x' por 'Y'. El símbolo blanco se denota con la letra 'B'")
    print(" - L: se mueve el cabezal en la dirección 'L', en donde 'L' es 'I' o 'D' (izquierda o derecha)");
    
    #ingresa el número de transiciones
    while True:
        try:
            nTransitions = int(input('\nIngrese el número de transiciones: '))
            break
        except ValueError:
            print('Error. Ingreso no válido.') 
    
    #inicializamos variables
    count = 1
    d={}
    
    for i in range(nTransitions):
        print('\n----- Transición',count,'-----')
        q = input('Ingrese q: ')
        x = input('Ingrese x: ')
        p = input('Ingrese p: ')
        Y = input('Ingrese Y: ')
        L = input('Ingrese L: ')
        print('d(',q,',',x,') = (',p,',',Y,',',L,')')

        d[(q,x)] = [p,Y,L]
        count = count+1
    
    #retorna un diccionario con las transiciones
    return d


# --- Función para transformar la palabra de un string a una lista ---
def createTape(word):
    #inicializamos variables
    tape = []
    blanks = []
    
    for i in word:
        tape.append(i)

    for i in range(100):
        blanks.append('B')

    tape = blanks + tape + blanks
    
    return tape


# --- Función que recorre las transiciones e imprime en pantalla si la palabra pertenece al lenguaje especificado o no ---
def TM(initial_state, final_state, d, word):
    try:
        #inicializamos variables
        pos = 100;
        tape = createTape(word)
        key = (initial_state, tape[pos])

        #actualizamos la cinta
        tape[pos] = d[key][1]

        #nos movemos un espacio a la izquierda
        if(d[key][2] == 'I' or d[key][2] == 'i'):
            pos = pos-1;

        #nos movemos un espacio a la derecha
        if(d[key][2] == 'D' or d[key][2] == 'd'):
            pos = pos+1;

        next_key = (d[key][0],tape[pos])

        while d[next_key][0] != final_state:
            key = next_key

            #actualizamos la cinta
            tape[pos] = d[key][1]
            #print('cinta:', tape)

            #nos movemos un espacio a la izquierda
            if(d[key][2] == 'I' or d[key][2] == 'i'):
                pos = pos-1;

            #nos movemos un espacio a la derecha
            if(d[key][2] == 'D' or d[key][2] == 'd'):
                pos = pos+1;

            next_key = (d[key][0],tape[pos])

            if(d[next_key][0] == final_state):
                print('La palabra', word, 'SI pertenece al lenguaje especificado.')

    except KeyError:
        print('La palabra', word, 'NO pertenece al lenguaje especificado.')


# --- Función que corre el programa ---
def run():
    ########## PASO 1: INGRESAR ESTADO INICIAL ####################
    initial_state = input('Ingrese el estado inicial: ')

    ########## PASO 2: INGRESAR ESTADO FINAL ######################
    final_state = input('Ingrese el estado final: ')

    ########## PASO 3: INGRESAR TRANSICIONES #######################
    d = transitions()

    ########## PASO 4: INGRESAR PALABRAS ###########################
    while True:
        word = input("\nIngrese palabra ('exit' para salir): ")
        if word == 'exit':
            break
        TM(initial_state, final_state, d, word)

    print('\nPrograma finalizado.')
    exit()

run()
