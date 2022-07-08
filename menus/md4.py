import threading
import hashlib

class Colors:
    red = '\033[31m'
    green = '\033[32m'
    cyan = '\033[36m'

def mainmd4():
    user_hash = input(Colors.green+"[+] Enter the md4 hash > ")
    pass_list = input(Colors.green+"[+] Enter path to wordlist > ")

    def file_Open(pass_list):
        global doc 
        try: 
            doc = open(pass_list, "r")
        except:
            exit(Colors.red+"[!] File not found ..")

    file_Open(pass_list)

    for word in doc:
        print(Colors.cyan+"[+] Trying : " + word.strip() + Colors.cyan)
        encode = word.encode("utf-8")
        md4_hash = hashlib.new('md4', encode.strip()).hexdigest()

        if md4_hash == user_hash:
            print(Colors.green+"\n[ Password found ] : "+ word)
            exit(0)

    print(Colors.red+"[!] Password not found in wordlist .")

x = threading.Thread(target=mainmd4)
x.start()