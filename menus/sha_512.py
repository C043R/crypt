import threading
import hashlib

class Colors:
    red = '\033[31m'
    cyan = '\033[36m'
    green = '\033[32m'

def sha512crack():
    user_hash = input(Colors.green+"[+] Enter sha512 hash > ")
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
        sha512_hash = hashlib.sha512(encode.strip()).hexdigest()

        if sha512_hash == user_hash:
            print(Colors.green+"\n[ Password found ] : " + word)
            exit(0)

    print(Colors.red+"[!] Password not found in wordlist or format is wrong .")

x = threading.Thread(target=sha512crack)
x.start()

    

