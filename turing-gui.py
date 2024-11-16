from tkinter import *
from threading import Thread
import tkinter as tk
from tkinter import messagebox

release = True
verdad=False
verdad3=False
def Palabra_correcta():
    messagebox.showinfo("Palabra","Su palabra pertenece a la MT!")
def Palabra_incorrecta():       
    messagebox.showinfo("Palabra","Su palabra NO pertenece a la MT")
    
def show_frame(d):
    d=transitions(q_valor.get(),x_valor.get(),p_valor.get(),Y_valor.get(),L_valor.get())
    q_valor.set('')
    x_valor.set('')
    p_valor.set('')
    Y_valor.set('')
    L_valor.set('')
def show_frame1(frame):
    frame.tkraise()
    
def show_frame2(frame):
    #frame.tkraise()
    while verdad3:
        frame.tkraise()
    
def click_callback(d):
    global release  
    release = False
    if not release and int(var1.get()) < numT.get():
        var1.set(str(int(var1.get())+1))
        release = True
    else:
         show_frame(d)
         show_frame1(frame3)

def reiniciar(d):
    d.clear()
    show_frame1(frame1)
    var1.set('1')
    print(d)


### Función para ingresar transiciones al diccionario ###
def transitions(q,x,p,Y,L): 
    d[(q,x)] = [p,Y,L]
    print(d)
    #retorna un diccionario con las transiciones
    return d
### Función para transformar la palabra de un string a una lista ###
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
### Función que recorre las transiciones e imprime en pantalla si la palabra pertenece al lenguaje especificado o no ###
def MT(initial_state, final_state, d, word):
    try:
        #inicializamos variables
        pos = 100;
        #Transforma StringVar a  String para poder trabajar con la palabra
        pala=word.get()
        tape = createTape(pala)
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

            #nos movemos un espacio a la izquierda
            if(d[key][2] == 'I' or d[key][2] == 'i'):
                pos = pos-1;

            #nos movemos un espacio a la derecha
            if(d[key][2] == 'D' or d[key][2] == 'd'):
                pos = pos+1;

            next_key = (d[key][0],tape[pos])

            if(d[next_key][0] == final_state):
                Palabra_correcta()

    except KeyError:
        Palabra_incorrecta()
#---- Creamos la ventana ------
window=tk.Tk()
window.title(" Tarea Automatas ")
window.state('zoomed')
window.rowconfigure(0,weight=1) 
window.columnconfigure(0,weight=1)
frame1=tk.Frame(window)
frame2=tk.Frame(window)
frame3=tk.Frame(window)

for frame in (frame1,frame2,frame3):
    frame.grid(row=0,column=0,sticky='nsew')

#---- Estos seran los valors de las transiciones d(p,x)=(p,Y,L)----
q_valor=StringVar()
x_valor=StringVar()
p_valor=StringVar()
Y_valor=StringVar()
L_valor=StringVar()

#----Creamos los frames de la ventana y sus cuadros de textos e ingreso de datos ----


#----Frame 1-----


#----Encabezado del programa -----
frame1_title=Label(frame1, text="Máquina de Turing", font=("Cambria",19), bg="#56CD63", fg="white", width="800", height="2")
frame1_title.pack(fill='x')
frame1_bg=Label(frame1,bg="#213141")
frame1_bg.pack(fill='both',expand='True')

estadoInicial=Label(frame1,text="Ingrese  el estado inicial: ", font=("Cambria",14),  bg="#FFEEDD",height="1")
estadoInicial.place(x=22 , y=180)
estadoFinal=Label(frame1,text="Ingrese  el estado Final: ", font=("Cambria",14),  bg="#FFEEDD",height="1")
estadoFinal.place(x=22 , y=300)
numTransitions=Label(frame1,text="Ingrese  el numero de transiciones: ", font=("Cambria",14),  bg="#FFEEDD",height="1")
numTransitions.place(x=22 , y=420)

#------ Creamos las variables para el ingreso de Estado Inicial, Estado Final y Numero de transiciones ----
estadoI = StringVar()
estadoF = StringVar()
numT= IntVar()

estadoI_entry = Entry(frame1,textvariable=estadoI, width="40")
estadoF_entry = Entry(frame1,textvariable=estadoF, width="40")
numT_entry = Entry(frame1,textvariable=numT,width="40")

estadoI_entry.place(x=350, y=185)
estadoF_entry.place(x=350, y=305)
numT_entry.place(x=350, y=425)
#---- creacion de boton para ingresar los datos, al presionarlo los datos ingresan al sistema----
frame1_btn=Button(frame1, text='Enter', command=lambda:show_frame1(frame2), width="30", height="2", bg="#00CD63")
frame1_btn.place(x=500,y=730)
show_frame1(frame1)



##----- Frame 2-----------------------------


#---Creamos el diccionario que contenera las transiciones ----
d={}

#----Repetimos el encabezado de el programa ----
frame2_title=Label(frame2, text="Máquina de Turing", font=("Cambria",19), bg="#56CD63", fg="white", width="800", height="2")
frame2_title.pack(fill='x')
frame2_bg=Label(frame2,bg="#213141")
frame2_bg.pack(fill='both',expand='True')

#----Cuadros de texto----
frame2_transiciones1 = Label(frame2, text="Procederá a escribir transiciones de la forma d(q,x)=(p,Y,L) en donde: ", font=("Cambria",14),  bg="#FFEEDD",height="1")
frame2_transiciones1.place(x=22,y=100)
frame2_transiciones2 = Label(frame2, text="q: estado actual", font=("Cambria",14),  bg="#FFEEDD",height="1")
frame2_transiciones2.place(x=22,y=140)
frame2_transiciones3 = Label(frame2, text="x: símbolo actual", font=("Cambria",14),  bg="#FFEEDD",height="1")
frame2_transiciones3.place(x=22,y=180)
frame2_transiciones4 = Label(frame2, text="p: se pasa de estado 'q' a estado 'p'", font=("Cambria",14),  bg="#FFEEDD",height="1")
frame2_transiciones4.place(x=22,y=220)
frame2_transiciones5 = Label(frame2, text="Y: se cambia el símbolo 'x' por 'Y'. El símbolo blanco se denota con la letra 'B'", font=("Cambria",14),  bg="#FFEEDD",height="1")
frame2_transiciones5.place(x=22,y=260)
frame2_transiciones6 = Label(frame2, text="L: se mueve el cabezal en la dirección 'L', en donde 'L' es 'I' o 'D' (izquierda o derecha)", font=("Cambria",14),  bg="#FFEEDD",height="1")
frame2_transiciones6.place(x=22,y=300)

#-----Cuadro de ingresar transicion, con var1 siendo el numero de la transicion actual-----
var=StringVar()
var1=StringVar()
var.set('Ingrese la transición: ')

frame2_transiciones7 = Label(frame2, textvariable= var,font=("Cambria",14),  bg="#FFEEDD",height="1")
frame2_transiciones7.place(x=22,y=360)
frame2_transiciones8 = Label(frame2, textvariable= var1,font=("Cambria",14),  bg="#FFEEDD",height="1")
frame2_transiciones8.place(x=189,y=360)

#-----Creacion de botones Enter y Terminado ------#
frame2_btn=Button(frame2, text='Enter', command=lambda:show_frame(frame2), width="30", height="2", bg="#00CD63")
frame2_btn.place(x=500,y=730)
frame2_btn.bind('<Button-1>', lambda e: Thread(target=click_callback(d), daemon=True).start())
var1.set('1')

#------Cuadros de texto -----#
frame2_transiciones9= Label(frame2, text="Ingrese q: ", font=("Cambria",14),  bg="#FFEEDD",height="1")
frame2_transiciones9.place(x=22,y=400)


frame2_transiciones9= Label(frame2, text="Ingrese x: ", font=("Cambria",14),  bg="#FFEEDD",height="1")
frame2_transiciones9.place(x=22,y=440)

frame2_transiciones9= Label(frame2, text="Ingrese p: ", font=("Cambria",14),  bg="#FFEEDD",height="1")
frame2_transiciones9.place(x=22,y=480)

frame2_transiciones9= Label(frame2, text="Ingrese Y: ", font=("Cambria",14),  bg="#FFEEDD",height="1")
frame2_transiciones9.place(x=22,y=520)

frame2_transiciones9= Label(frame2, text="Ingrese L: ", font=("Cambria",14),  bg="#FFEEDD",height="1")
frame2_transiciones9.place(x=22,y=560)

#--------Ingreso de los datos de las transiciones ----#
q_entry = Entry(frame2,textvariable=q_valor, width="40")
q_entry.place(x=125, y=405)

x_entry = Entry(frame2,textvariable=x_valor, width="40")
x_entry.place(x=125, y=445)

p_entry = Entry(frame2,textvariable=p_valor, width="40")
p_entry.place(x=125, y=485)

Y_entry = Entry(frame2,textvariable=Y_valor, width="40")
Y_entry.place(x=125, y=525)

L_entry = Entry(frame2,textvariable=L_valor, width="40")
L_entry.place(x=125, y=565)


show_frame1(frame1)
#paso a frame 3



#---- Frame 3 -------------------------



#------Repetimos el encabezado del programa ----

frame3_title=Label(frame3, text="Máquina de Turing", font=("Cambria",30), bg="#56CD63", fg="white", width="800", height="2")
frame3_title.pack(fill='x')
frame3_bg=Label(frame3,bg="#213141")
frame3_bg.pack(fill='both',expand='True')

#-----Cuadro de texto ----#
frame3_palabra = Label(frame3, text="Ingrese la palabra a revisar: ", font=("Cambria",14),  bg="#FFEEDD",height="2")
frame3_palabra.place(x=22,y=300)

#-----Ingreso de la palabra -----#
palabra=StringVar()

palabra_entry = Entry(frame3,textvariable=palabra, width="40")
palabra_entry.place(x=280, y=315)

#------Creacion boton "Revisar"------
frame3_btn=Button(frame3, text='Revisar', command=lambda:MT(estadoI.get(),estadoF.get(),d,palabra), width="30", height="2", bg="#00CD63")
frame3_btn.place(x=500,y=730)

#------Creacion boton "Ingresar nueva maquina"-------
frame3_btn2=Button(frame3, text='Ingresar nueva máquina',width="30", height="2", bg="#00CD63")
frame3_btn2.bind('<Button-1>', lambda e: Thread(target=reiniciar(d), daemon=True).start())
frame3_btn2.place(x=900,y=730)

show_frame1(frame1)

window.mainloop()
