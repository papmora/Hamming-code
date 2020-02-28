
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, RAISED
from tkinter.ttk import Frame, Label, Entry, Button, Style
#from Converter import *

DreiBits = ["000", "001", "010", "011", "100", "101", "110", "111"]

def Oct_to_bin(num):
    temp = str(num)
    temp_ans = ""
    i=0
    
    while i < len(temp):
        temp_ans += DreiBits[int(temp[i])]
        i+=1
    return str(temp_ans)
class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Input", width=6)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)
        
        def test():
            s = entry1.get()
            print (s)
            print (str(Oct_to_bin((s))))

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)

        hammingButton = Button(self, text="Hamming", command = test)
        hammingButton.pack(side=RIGHT, padx=5, pady=5)
        nrzButton = Button(self, text="NRZ")
        nrzButton.pack(side=RIGHT, padx=5, pady=5)
        conversionButton = Button(self, text="Conversion")
        conversionButton.pack(side=RIGHT)

        
def main():

    root = Tk()
    root.geometry("300x200+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
