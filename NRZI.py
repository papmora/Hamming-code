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

f=input()
x=bin(int(f,16))[2:] #Input hex, lo convierte a decimal y luego a binario, lo guarda en "x"
if (len(x)%4 != 0):
    x=bin(int(f,16))[2:].zfill(len(x)+(4-(len(x)%4)))  #rellenar los ceros faltantes al pasarlo a binario

for i in x:
   a.append(i)
y=NRZI1(x,y)


plt.xticks(range(len(x)),a), plt.yticks([0]), plt.step(range(len(x)),y, where='post') #grafico 
plt.show()

#print(x) #para test, valor en binario del numero hex


input('Press enter to close') 



