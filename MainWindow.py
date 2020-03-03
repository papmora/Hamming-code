
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, RAISED, BOTTOM
from tkinter.ttk import Frame, Label, Entry, Button, Style
from tkinter import *
from tkinter import messagebox
from Hexa import *

#from Converter import *


############################################################################
############Definicion de funciones y elementos necesarios##################

##Array que contiene el equivalente en 3 bits binarios de los numeros del 1 al 7
DreiBits = ["000", "001", "010", "011", "100", "101", "110", "111"]


##Funcion principal de conversion
##Revisa que la entrada sea correcta

def converter(octal):       
    temp = int(octal)
    if check(temp):
        return Oct_to_bin(octal)
    else:
        print("ingrese otro numero")


##Funcion auxiliar que revisa el numero de digitos de la entrada
##Tmabien revisa si corresponde todo a digitos octales
        
def check(number):
    i = 0
    m=len(str(number))
    while i < m:
        if (number%10)/8 >= 1:
            return False 
        else:
            number = number//10
            i+=1
    return True


##Funcion de conversion de Base 8 a Binario

def Oct_to_bin(num):
    temp = str(num)
    temp_ans = ""
    i=0
    
    while i < len(temp):
        temp_ans += DreiBits[int(temp[i])]
        i+=1
    return str(temp_ans)






##--------------------------------------------------------------Hamming code-------------------------------------------------------------------------------##

def calcRedundantBits(m): 

        # Se usa la formula 2 ^ r >= m + r + 1 
        # para calcular los bits redundantes.
        for i in range(m): 
                if(2**i >= m + i + 1): 
                        return i 


def posRedundantBits(data, r): 

        # Los bits redundantes se colocan en la posicion que 
        # le corresponde segun su potencia de 2.
        j = 0
        k = 0
        m = len(data) 
        res = '' 

        # Se inserta un '0' si la posicion es potencia de 2 
        # sino se ingresa un dato del binario ingresado 
        for i in range(1, m + r+1): 
                if(i == 2**j): 
                        res = res + '0'
                        j += 1
                else: 
                        res = res + data[k] 
                        k += 1

        # los resultados se revierten ya que se cuenta
        # hacia atrás (m + r+1 ... 1)
        print(res[::-1])
        return res[::-1] 


def calcParityBits(arr, r):
        n = len(arr)
        # Crea ventana de la tabla
        master = Tk()

        # Crea las etiquetas de la tabla
        l1 = Label(master, text = "").grid(row = 0, column = 0, sticky = W, pady = 2) 
        l2 = Label(master, text = "Palabras de datos(sin paridad):").grid(row = 1, column = 0, sticky = W, pady = 2)
        l3 = Label(master, text = "P1").grid(row = 2, column = 0, sticky = W, pady = 2)
        l4 = Label(master, text = "P2").grid(row = 3, column = 0, sticky = W, pady = 2)
        l5 = Label(master, text = "P3").grid(row = 4, column = 0, sticky = W, pady = 2)
        l6 = Label(master, text = "P4").grid(row = 5, column = 0, sticky = W, pady = 2)
        l7 = Label(master, text = "P5").grid(row = 6, column = 0, sticky = W, pady = 2)
        l8 = Label(master, text = "Palabras de datos(con paridad):").grid(row = 7, column = 0, sticky = W, pady = 2)
         
        c2 = Label(master, text = "D12").grid(row = 0, column = 1, sticky = W, pady = 2)
        c3 = Label(master, text = "P5").grid(row = 0, column = 2, sticky = W, pady = 2)
        c4 = Label(master, text = "D11").grid(row = 0, column = 3, sticky = W, pady = 2)
        c5 = Label(master, text = "D10").grid(row = 0, column = 4, sticky = W, pady = 2)
        c6 = Label(master, text = "D9").grid(row = 0, column = 5, sticky = W, pady = 2)
        c7 = Label(master, text = "D8").grid(row = 0, column = 6, sticky = W, pady = 2)
        c8 = Label(master, text = "D7").grid(row = 0, column = 7, sticky = W, pady = 2)
        c9 = Label(master, text = "D6").grid(row = 0, column = 8, sticky = W, pady = 2) 
        c10 = Label(master, text = "D5").grid(row = 0, column = 9, sticky = W, pady = 2)
        c11 = Label(master, text = "P4").grid(row = 0, column = 10, sticky = W, pady = 2)
        c12 = Label(master, text = "D4").grid(row = 0, column = 11, sticky = W, pady = 2)
        c13 = Label(master, text = "D3").grid(row = 0, column = 12, sticky = W, pady = 2)
        c14 = Label(master, text = "D2").grid(row = 0, column = 13, sticky = W, pady = 2)
        c15 = Label(master, text = "P3").grid(row = 0, column = 14, sticky = W, pady = 2)
        c16 = Label(master, text = "D1").grid(row = 0, column = 15, sticky = W, pady = 2)
        c17 = Label(master, text = "P2").grid(row = 0, column = 16, sticky = W, pady = 2)
        c18 = Label(master, text = "P1").grid(row = 0, column = 17, sticky = W, pady = 2)
        
        for m in range(1, n+1):
                        Label(master, text = arr[m-1]).grid(row = 1, column = m, sticky = W, pady = 8)

        # Se encuentran los bits de paridad, iterando de 
        # 0 a r - 1 
        for i in range(r): 
                val = 0
                
                for j in range(1, n+1): 

                        # Si hay un 1 en la posicion significativa segun el bit
                        # de paridad entonces se aplica Bitwise XOR (^) en el valor del array  
                        # para encontrar el valor del bit de paridad
                        if(j & (2**i) == (2**i)): 
                                val = val ^ int(arr[-1*j])
                                # -1 * j ya que el array esta al reves

                # Se concatena el String 
                # (0 a n - 2^r) + bit de paridad + (n - 2^r + 1 a n) 
                arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
                print(arr)
                for k in range(1, n+1):
                        Label(master, text = arr[k-1]).grid(row = i+2, column = k, sticky = W, pady = 8)
                
        for p in range(1, n+1):
                        Label(master, text = arr[p-1]).grid(row = 7, column = p, sticky = W, pady = 8)
        return arr 


def detectError(arr, nr): 
        n = len(arr) 
        res = 0

        # Crea ventana de la tabla 
        master = Tk()

        # Crea etiquetas de la tabla 
        l1 = Label(master, text = "").grid(row = 0, column = 0, sticky = W, pady = 2) 
        l2 = Label(master, text = "Palabras de datos(sin paridad):").grid(row = 1, column = 0, sticky = W, pady = 2)
        l3 = Label(master, text = "P1").grid(row = 2, column = 0, sticky = W, pady = 2)
        l4 = Label(master, text = "P2").grid(row = 3, column = 0, sticky = W, pady = 2)
        l5 = Label(master, text = "P3").grid(row = 4, column = 0, sticky = W, pady = 2)
        l6 = Label(master, text = "P4").grid(row = 5, column = 0, sticky = W, pady = 2)
        l7 = Label(master, text = "P5").grid(row = 6, column = 0, sticky = W, pady = 2)
         
        c2 = Label(master, text = "D12").grid(row = 0, column = 1, sticky = W, pady = 2)
        c3 = Label(master, text = "P5").grid(row = 0, column = 2, sticky = W, pady = 2)
        c4 = Label(master, text = "D11").grid(row = 0, column = 3, sticky = W, pady = 2)
        c5 = Label(master, text = "D10").grid(row = 0, column = 4, sticky = W, pady = 2)
        c6 = Label(master, text = "D9").grid(row = 0, column = 5, sticky = W, pady = 2)
        c7 = Label(master, text = "D8").grid(row = 0, column = 6, sticky = W, pady = 2)
        c8 = Label(master, text = "D7").grid(row = 0, column = 7, sticky = W, pady = 2)
        c9 = Label(master, text = "D6").grid(row = 0, column = 8, sticky = W, pady = 2) 
        c10 = Label(master, text = "D5").grid(row = 0, column = 9, sticky = W, pady = 2)
        c11 = Label(master, text = "P4").grid(row = 0, column = 10, sticky = W, pady = 2)
        c12 = Label(master, text = "D4").grid(row = 0, column = 11, sticky = W, pady = 2)
        c13 = Label(master, text = "D3").grid(row = 0, column = 12, sticky = W, pady = 2)
        c14 = Label(master, text = "D2").grid(row = 0, column = 13, sticky = W, pady = 2)
        c15 = Label(master, text = "P3").grid(row = 0, column = 14, sticky = W, pady = 2)
        c16 = Label(master, text = "D1").grid(row = 0, column = 15, sticky = W, pady = 2)
        c17 = Label(master, text = "P2").grid(row = 0, column = 16, sticky = W, pady = 2)
        c18 = Label(master, text = "P1").grid(row = 0, column = 17, sticky = W, pady = 2)

        p1= Label(master, text = "Bit de paridad").grid(row = 0, column = 19, sticky = W, pady = 2)
        
        for m in range(1, n+1):
                        Label(master, text = arr[m-1]).grid(row = 1, column = m, sticky = W, pady = 8)

        # Calculamos los bits de paridad de nuevo 
        for i in range(nr): 
                val = 0
                for j in range(1, n + 1): 
                        if(j & (2**i) == (2**i)): 
                                val = val ^ int(arr[-1 * j])

                # Se concatena el String 
                # (0 a n - 2^r) + bit de paridad + (n - 2^r + 1 a n) 
                arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
                print(arr)
                for k in range(1, n+1):
                        Label(master, text = arr[k-1]).grid(row = i+2, column = k, sticky = W, pady = 8)

                # creamos un numero binarios uniendo los bits de paridad 
                res = res + val*(10**i)
        if (res == 0):
            print(messagebox.showinfo(message="No hay error", title="Error"))
        else:
            for t in range(0, len(str(res))):
                Label(master, text = str(res)[t]).grid(row = t+2, column = 19, sticky = E, pady = 8)
            # Convertimos binario a decimal
            return int(str(res), 2)
        







##########GUI############

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        
        binaryUpdater = StringVar()  #String variable to update the binary label
        binaryUpdater.set('***')
        
        hexUpdater = StringVar()  #String variable to update the hex label
        hexUpdater.set('***')
        
        self.master.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Valid inputs are 4 digit numbers in base 8", width=42)
        lbl1.pack( padx=5, pady=5)
    
        lbl2 = Label(frame1, textvariable = hexUpdater, width=20)
        lbl2.place(x=200, y=200)
        lbl2.pack(side = BOTTOM)

        lbl3 = Label(frame1, text = "Hexa", width=6)
        lbl3.place(x=200, y=200)
        lbl3.pack(side = BOTTOM)

        lbl4 = Label(frame1, textvariable = binaryUpdater, width=20)
        lbl4.place(x=200, y=200)
        lbl4.pack(side = BOTTOM,expand=True)

        lbl5 = Label(frame1, text= "Binario", width=6)
        lbl5.place(x=200, y=200)
        lbl5.pack(side = BOTTOM)
        
        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5,pady=10, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        l1= Label(frame2, text="Dato a transferir:")
        l1.place(x=200, y=200)
        l1.pack()
        entryText = StringVar() 
        entry3 = Entry(frame2, textvariable=entryText )
        entry3.pack(fill=X, expand=True)
        l3=Label(frame2, text="Dato con error:")
        l3.place(x=200, y=200)
        l3.pack()
        entry2 = Entry(frame2)
        entry2.pack(fill=X, expand=True)
        
        def updateUpdaters():  #function to update the text holders for the hex and binary labels
            s = entry1.get()
            if len(s) != 4 or check(int(s))== False:
                binaryUpdater.set("Invalid input")
                hexUpdater.set("Invalid input")
            else:
                print (s)
                binaryUpdater.set(str(converter((s))))
                temp = str(converter((s)))
                hexUpdater.set(str(binarioHexa(temp)))

        def hammingCode():
            
            
            s = entry1.get()
            if len(s) != 4 or check(int(s))== False:
                binaryUpdater.set("Invalid input")
                hexUpdater.set("Invalid input")
            else:
                # Se ingresa el dato que sera transmitido 
                data = str(converter(s))
        

                # Calcula el numero de bits redundantes necesarios
                m = len(data) 
                r = calcRedundantBits(m) 

                # Determina la posicion de los bits de redundantes 
                arr = posRedundantBits(data, r) 

                # Determina los bits de paridad
                arr = calcParityBits(arr, r)
                entryText.set(arr)

                           

                

        def hammingError():
            arr = entry2.get()

            s = entry1.get()

            # Se ingresa el dato que sera transmitido 
            data = str(converter(s))
        

            # Calcula el numero de bits redundantes necesarios
            m = len(data) 
            r = calcRedundantBits(m)
                        
            # Genera error en transmision al cambiar 
            # el valor de un bit.

            
            #arr = '01111111111111110'
            print("Error Data is " + arr) 
            correction = detectError(arr, r)
            print(messagebox.showinfo(message="El error esta en la posicion " + str(correction), title="Posicion"))
            

        def NRZI_action(): #function to plot the NRZI graphic
            
            s = entry1.get()
            if len(s) != 4 or check(int(s))== False:
                binaryUpdater.set("Invalid input")
                hexUpdater.set("Invalid input")
            else:
                binaryUpdater.set("-")
                hexUpdater.set("-")
                def NRZI1(v,w):
                    bit=-1
                    for i in v:
                        if int(i) == 0:
                            bit=bit
                        else:
                            bit=-bit 
                        w.append(bit)
                    return w

                from matplotlib import pyplot as plt
                y=[] 
                a=[]   #Aqui se va a guardar el arreglo para la grafica NRZI

                x= str(Oct_to_bin(entry1.get()))
                print (x)
                for i in x:
                   a.append(i)
                y=NRZI1(x,y)


                plt.xticks(range(len(x)),a), plt.yticks([0]), plt.step(range(len(x)),y, where='post') #grafico 
                plt.show()
            

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)

        hammingButton = Button(self, text="Hamming", command = hammingCode)
        hammingButton.pack(side=RIGHT, padx=5, pady=5)
        nrzButton = Button(self, text="NRZ", command = NRZI_action)
        nrzButton.pack(side=RIGHT, padx=5, pady=5)
        conversionButton = Button(self, text="Conversion",command = updateUpdaters)
        conversionButton.pack(side=RIGHT)
        hammingError = Button(frame2, text="Buscar error", width=50, command = hammingError)
        hammingError.pack(pady=5)

        
def main():

    root = Tk()
    root.geometry("300x350+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
