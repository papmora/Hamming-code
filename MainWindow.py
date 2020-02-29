
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, RAISED, BOTTOM
from tkinter.ttk import Frame, Label, Entry, Button, Style
from tkinter import *
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
        print("convertir a binario")
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





##########GUI############

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        
        binaryUpdater = StringVar()
        binaryUpdater.set('hi')
        
        hexUpdater = StringVar()
        hexUpdater.set('hi')
        
        self.master.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Input", width=6)
        lbl1.pack(side=LEFT, padx=5, pady=5)
    
        lbl2 = Label(frame1, textvariable = hexUpdater, width=12)
        lbl2.place(x=200, y=200)
        lbl2.pack(side = BOTTOM)

        lbl3 = Label(frame1, text = "Hexa", width=6)
        lbl3.place(x=200, y=200)
        lbl3.pack(side = BOTTOM)

        lbl4 = Label(frame1, textvariable = binaryUpdater, width=12)
        lbl4.place(x=200, y=200)
        lbl4.pack(side = BOTTOM,expand=True)

        lbl5 = Label(frame1, text= "Binario", width=6)
        lbl5.place(x=200, y=200)
        lbl5.pack(side = BOTTOM)
        
        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5,pady=10, expand=True)
        
        def updateUpdaters():
            s = entry1.get()
            if len(s) != 4:
                print ("Insert a 4 digit number")
            else:
                print (s)
                print (str(Oct_to_bin((s))))
                binaryUpdater.set(str(converter((s))))
                temp = str(converter((s)))
                hexUpdater.set(str(binarioHexa(temp)))


        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)

        hammingButton = Button(self, text="Hamming")
        hammingButton.pack(side=RIGHT, padx=5, pady=5)
        nrzButton = Button(self, text="NRZ")
        nrzButton.pack(side=RIGHT, padx=5, pady=5)
        conversionButton = Button(self, text="Conversion",command = updateUpdaters)
        conversionButton.pack(side=RIGHT)

        
def main():

    root = Tk()
    root.geometry("300x200+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
