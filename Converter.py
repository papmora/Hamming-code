DreiBits = ["000", "001", "010", "011", "100", "101", "110", "111"]
VierBits = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111"]

def converter(octal):
    if check(octal):
        print("convertir a binario")
    else:
        print("ingrese otro numero")


def check(number):
    i = 0
    m=len(str(number))
    if m > 4:
        return False
    while i < m:
        if (number%10)/8 >= 1:
            return False 
        else:
            number = number//10
            i+=1
    return True


def Oct_to_bin(num):
    temp = str(num)
    temp_ans = ""
    i=0
    while i < len(temp):
        temp_ans += DreiBits[int(temp[i])]
        i+=1
    return int(temp_ans)
