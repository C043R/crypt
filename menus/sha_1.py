import threading
import hashlib

class Colors:
    red = '\033[31m'
    green = '\033[32m'
    cyan = '\033[36m'

def sha1crack():
    user_hash = input(Colors.green+"[+] Enter sha1 hash > ")
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
        sha1_hash = hashlib.sha1(encode.strip()).hexdigest()

        if sha1_hash == user_hash:
            print(Colors.green+"\n[ Password found ] : "+ word)
            exit(0)

    print(Colors.red+"[!] Password not found in wordlist .")

x = threading.Thread(target=sha1crack)
x.start()
