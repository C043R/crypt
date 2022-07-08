class Colors:
    green = '\033[32m'
    blue = '\033[34m'
    cyan = '\033[36m'
    white = '\033[37m'


def encrypt(entry, s):
    result = ""

    for i in range(len(entry)):
        char = entry[i]

        if char.isupper():
            result += chr((ord(char) + s -65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def ceasarencrypt():
    entry = input(Colors.green+"[+] Enter string you want to encrypt > ")

    s = int(input(Colors.green+"[+] Enter shift number ( 1:default ) > "))

    def num():
        num_shifts = int(input(Colors.green + "[+] Enter number of shifts [example : 1-10] > "))
        print(Colors.white+"[+] Shift : 0 " + Colors.green+"Ciphertext :" + entry)

        counter = 0
        for j in range(0, num_shifts):
            counter += 1
            s = counter
            print(Colors.white+"[+] Shift : " + str(counter) + Colors.green+" Ciphertext : " + encrypt(entry,s))
            
    question = input(Colors.blue+"[+] Do you want to encrypt your string with multiple shifts ? (y/n) > ")

    if question == "y":
        num()  
    else:
        print(Colors.green+"[==================== [Results] ====================]")
        print(Colors.white+"[+] Given Text  : " + entry)
        print(Colors.blue+"[+] Shift : " + str(s))
        print(Colors.white+"[+] Cipher Text : " + encrypt(entry,s))
        print(Colors.green+"[==================== [Results] ====================]")


def ceasardecrypt():
    entry = input(Colors.green+"[+] Enter string you want to decrypt > ")


    def num():
        num_shifts = int(input(Colors.green+"[+] Enter number of shifts [example : 1-10] > "))
        print(Colors.white+"[+] Shift : 0 " + Colors.green+"Ciphertext :" + entry)

        s = 0 
        counter = 0
        for j in range (0 ,num_shifts):
            counter += 1
            s = counter
            print(Colors.white+"[+] Shift : " + str(counter) + Colors.green+" Ciphertext : " + encrypt(entry,s))
            
    question = input(Colors.blue+"[+] Do you want to decrypt your string with multiple shifts ? (y/n) > ")

    if question == "y":
        num()  
    else:
        s = int(input(Colors.green+"[+] Enter shift number ( 1:default ) > "))
        
        print(Colors.green+"[==================== [Results] ====================]")
        print(Colors.white+"[+] Given Text  : " + entry)
        print(Colors.blue+"[+] Shift : " + str(s))
        print(Colors.white+"[+] Cipher Text : " + encrypt(entry,s))
        print(Colors.green+"[==================== [Results] ====================]")

