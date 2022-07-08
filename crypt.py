import threading
import signal
import requests
import platform
import urllib
import time 
import sys
import os

sys.dont_write_bytecode = True


class Colors:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'


def keyboard():
    ask = input(Colors.red+"[ Detected CTRL+C ] Do you really want to exit (y/n) ? > ")
    if ask == "y":
        exit(Colors.green+"[!] Goodbye ...")
    elif ask == "n":
        menu()
    else:
        print(Colors.red+"[!] Invalid option , reloading .. ")
        time.sleep(2)
        keyboard()


def connect():
    print(Colors.blue+"[+] Checking internet connection ....")
    try:
        request = requests.get('https://google.com', timeout=3)
        print(Colors.blue + "Connection established" + Colors.blue + "[" + Colors.green + '\u2713' + Colors.blue + "]")
    except (requests.ConnectionError, requests.Timeout) as exception:
        print(Colors.red+"[!] No internet connection.")

try:
    import base58
    import hashlib
    import base64

except ImportError or ModuleNotFoundError:
    def modules_exist():
        q = input(Colors.red + "[Error : Module not found] Run setup file (y/n)? > ")
        if q == "y":
            connect()
            if platform.system() == "Linux":
                print(Colors.green + "[!] Running linux setup file .")
                os.system("bash setup.sh")
            elif platform.system() == "Windows":
                print(Colors.green+"[!] Running windows setup file .")
                os.system("setup.bat")
        elif q == "n":
            print(Colors.red + "[!] Exiting..")
            exit(0)
        else:
            print(Colors.red + "[!] Please provide a valid input ,reloading ..")
            modules_exist()

    modules_exist()

utf = Colors.magenta+"[ Encoding : Utf-8 ]"


def banner():
        print(Colors.red+f"""
        
{Colors.red} ██████╗██████╗ ██╗   ██╗██████╗ ████████╗     {Colors.magenta}   ___..-.
{Colors.red}██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚═ ██╔══╝     {Colors.magenta}._/  __ \_`-.__                        
{Colors.red}██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║        {Colors.magenta}/ .'/###\_ `-.  \--. 
{Colors.red}██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║        {Colors.magenta}/.-_/#####\  /-' `\_ , 
{Colors.red}╚██████╗██║  ██║   ██║   ██║        ██║        {Colors.magenta}/- / ######\_  \._   `-,
{Colors.red} ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝        {Colors.magenta}---" "'"''"'"'''" ''"'"''"

{Colors.red}    Developed by @kodurrrr                     {utf}
        """)

try: 
    def menu():
        banner()
        print(Colors.green+"[1] Encrypt")
        print(Colors.green+"[2] Decrypt")
        print(Colors.green+"[3] Exit")
        print("")

        option = input(Colors.green+"[+] Choose an option > ")
        if option == "1":
            def encr():

                print(Colors.red+"""
    ____                       __  _             
    / __/__  __________ _____  / /_(_)__  ___     
    / _// _ \/ __/ __/ // / _ \/ __/ / _ \/ _ \    
    /___/_//_/\__/_/  \_, / .__/\__/_/\___/_//_/    
                    /___/_/                     """)   

                print(Colors.green+"""
    |==================================|

    [1] Md4           [12] Rot13
    [2] Md5           [13] Rot18
    [3] Sha1          [14] Rot47
    [4] Sha256        [15] Binary
    [5] Sha384        [16] Base85
    [6] Sha512        [17] Base16
    [7] Base32        [18] Ceaser
    [8] Base58        [19] Go back
    [9] Base64        [20] Exit
    [10] Baconian     
    [11] Atbash       

    |===================================|
    """)

                encryption = input(Colors.green+"[+] Choose a cipher > ")

                if encryption == "1":
                    entry = input(Colors.green+"[+] Enter string you want to encrypt > ")
                    ob = hashlib.new('md4', entry.encode('utf-8'))
                    digest = ob.hexdigest()
                    print(Colors.blue+"[+] MD4 : "+digest)

                elif encryption == "2":
                    entry = input(Colors.green+"[+] Enter string you want to encrypt > ")
                    ob = hashlib.new('md5', entry.encode('utf-8'))
                    digest = ob.hexdigest()
                    print(Colors.blue+"[+] MD5 : "+digest)

                elif encryption == "3":
                    entry = input(Colors.green+"[+] Enter string you want to encrypt > ")
                    hash_object = hashlib.sha1(entry.encode('utf-8'))
                    hex_dig = hash_object.hexdigest()
                    print(Colors.blue+"[+] Sha1 : "+hex_dig) 

                elif encryption == "4":
                    entry = input(Colors.green+"[+] Enter string you want to encrypt > ")
                    hash_object = hashlib.sha256(entry.encode('utf-8'))
                    hash_256 = hash_object.hexdigest()
                    print(Colors.blue+"[+] Sha256 : " + hash_256)
                
                elif encryption == "5":
                    entry = input(Colors.green+"[+] Enter string you want to encrypt > ")
                    hash_object = hashlib.sha384(entry.encode('utf-8'))
                    hash_384 = hash_object.hexdigest()
                    print(Colors.blue+"[+] Sha384 : " + hash_384)

                elif encryption == "6":
                    entry = input(Colors.green+"[+] Enter string you want to encrypt > ")
                    hash_object = hashlib.sha512(entry.encode('utf-8'))
                    hash_512 = hash_object.hexdigest()
                    print(Colors.blue+"[+] Sha512 : " + hash_512)

                elif encryption == "7":
                    entry = input(Colors.green+"[+] Enter string you want to encode > ")
                    print(Colors.blue+"[+] Base32 : "+base64.b32encode(bytearray('{entry}', 'ascii')).decode('utf-8'))

                elif encryption == "8": 
                    entry = input(Colors.green+"[+] Enter string you want to encode >")
                    base58Str = base58.b58encode(entry.encode('utf-8')).decode('utf-8')
                    print(Colors.blue+"[+] Base58 : "+base58Str)
                
                elif encryption == "9":
                    entry = input(Colors.green+"[+] Enter string you want to encode >")
                    message_bytes = entry.encode('utf-8')
                    base64_bytes = base64.b64encode(message_bytes)
                    base64_message = base64_bytes.decode('utf-8')
                    print(Colors.blue+"[+] Base64 : "+base64_message)

                elif encryption == "10":
                    from modules.baconian import encrypt
                    entry = input(Colors.green+"[+] Enter string you want to encrypt >")
                    print(Colors.blue+"[+] Baconian : "+encrypt(entry))

                elif encryption == "11":
                    from modules.atbash import atbash
                    entry = input(Colors.green+"[+] Enter string you want to encrypt > ")
                    print(Colors.blue+"[+] Atbash : " + (atbash(entry)))

                elif encryption == "12":
                    from modules.rot13 import Rot13
                    entry = input(Colors.green+"[+] Enter string you want to encrypt > ")
                    print(Colors.blue+"[+] Rot13 : " + Rot13(entry))
                
                elif encryption == "13":
                    from modules.rot18 import rot18
                    text = input(Colors.green+"[+] Enter string you want to encrypt > ")
                    rot18(text)
                    
                elif encryption == "14":
                    from modules.rot47 import rot47
                    entry = input(Colors.green+"[+] Enter string you want to encrypt > ")
                    print(Colors.blue+"[+] Rot47 : " + rot47(entry))

                elif encryption == "15":
                    entry = input(Colors.green+"[+] Enter string you want to encode > ")
                    binary = ' '.join(format(x, 'b') for x in bytearray(entry, 'utf-8'))
                    print(Colors.blue+"[+] Binary : " + binary)

                elif encryption == "16":
                    entry = input(Colors.green+"[+] Enter string you want to encode > ")
                    b = entry.encode("UTF-8")
                    e = base64.b85encode(b)
                    d = e.decode("UTF-8")
                    print(Colors.blue+"[+] Base85 :", d)

                elif encryption == "17":
                    entry = input(Colors.green+"[+] Enter string you want to encode > ")
                    b = entry.encode("UTF-8")
                    e = base64.b16encode(b)
                    s1 = e.decode("UTF-8")
                    print(Colors.blue+"[+] Base16 : ", s1)               

                elif encryption == "18":
                    from modules.ceasar import ceasarencrypt
                    ceasarencrypt()

                elif encryption == "19":
                    print(Colors.blue+"[+] Going back ..")
                    menu() 

                elif encryption == "21":
                    exit(Colors.red+"[+] Exiting ...")
            encr()

        elif option == "2":
            def decryption():
                print(Colors.red+"""
    ___                        __  _        
    / _ \___ __________ _____  / /_(_)__  ____ 
    / // / -_) __/ __/ // / _ \/ __/ / _ \/ _ |  
    /____/\__/\__/_/  \_, / .__/\__/_/\___/_//_/
                    /___/_/                    """)

                print(Colors.green+"""
    |==================================|

    [1] Md4           [12] Rot13
    [2] Md5           [13] Rot18
    [3] Sha1          [14] Rot47
    [4] Sha256        [15] Binary
    [5] Sha384        [16] Base85
    [6] Sha512        [17] Base16
    [7] Base32        [18] Ceaser
    [8] Base58        [19] Go back
    [9] Base64        [20] Exit
    [10] Baconian     
    [11] Atbash       

    |===================================|
    """)

                decr = input(Colors.green+"[+] Choose a cipher > ")

                if decr == "1":
                    from menus.md4 import md4_menu
                    md4_menu()

                elif decr == "2":
                    from menus.md5 import md5_menu
                    md5_menu()

                elif decr == "3":
                    from menus.sha_1 import sha1
                    sha1()

                elif decr == "4":
                    from menus.sha_256 import sha256
                    sha256()

                elif decr == "5":
                    from menus.sha_384 import sha384
                    sha384()

                elif decr == "6":
                    from menus.sha_512 import sha512
                    sha512()
                    
                elif decr == "7":
                    entry = input(Colors.green+"[+] Enter base32 encoded string > ")
                    print(Colors.blue+"[+] Base32 : "+base64.b32decode(bytearray('{entry}', 'ascii')).decode('utf-8'))
                
                elif decr == "8":
                    base58 = input(Colors.green+"[+] Enter base58 encoded string > ")
                    message = base58.b58decode(base58).decode('utf-8')
                    print(Colors.red+"[+] Decoded message : "+message)

                elif decr == "9":
                    base64_message = input(Colors.green+"[+] Enter base64 encoded string > ")
                    base64_bytes = base64_message.encode('ascii')
                    message_bytes = base64.b64decode(base64_bytes)
                    message = message_bytes.decode('ascii')
                    print(Colors.red+"[+] Decoded message : "+message)

                elif decr == "10":
                    from modules.baconian import decrypt
                    entry = input(Colors.green+"[+] Enter string you want to decrypt >")
                    print(Colors.blue+"[+] Baconian : "+decrypt(entry))

                elif decr == "11":
                    from modules.atbash import atbash
                    entry = input(Colors.green+"[+] Enter atbash encoded string > ")
                    print(Colors.blue+"[+] Decoded message : " + (atbash(entry)))

                elif decr == "12":
                    from modules.rot13 import Rot13
                    entry = input(Colors.green+"[+] Enter string you want to decrypt > ")
                    print(Colors.blue+"[+] Rot13 : " + Rot13(entry))

                elif decr == "13":
                    from modules.rot18 import rot18
                    text = input(Colors.green+"[+] Enter string you want to decrypt > ")
                    rot18(text)

                elif decr == "14":
                    from modules.rot47 import rot47
                    entry = input(Colors.green+"[+] Enter string you want to decrypt > ")
                    print(Colors.blue+"[+] Rot47 : " + rot47(entry))

                elif decr == "15":
                    from modules.binary import decode_binary_string
                    text = input(Colors.green+"[+] Enter binary string > ")
                    print(Colors.blue+"[+] Decoded message : " + decode_binary_string(text))

                elif decr == "16":
                    base_85 = input(Colors.green+"[+] Enter base85 encoded string > ")
                    b1 = base_85.encode("UTF-8")
                    d = base64.b85decode(b1)
                    s2 = d.decode("UTF-8")
                    print(Colors.blue+"[+] Decoded message : ", s2)

                elif decr == "17":
                    base_16 = input(Colors.green+"[+] Enter base16 encoded string > ")
                    b = base_16.encode("UTF-8")
                    e = base64.b16encode(b)
                    s1 = e.decode("UTF-8")
                    print("[+] Decoded message : ", s1)

                elif decr == "18":
                    from modules.ceasar import ceasardecrypt
                    ceasardecrypt()

                elif decr == "19":
                    print(Colors.blue+"[+] Going back ..")
                    menu()
                elif decr == "20":
                    exit(Colors.red+"[!] Exiting ...")

            decryption()

        elif option == "3":
            exit(Colors.red+"[!] Exiting ...")

        elif option == "clear":
            if platform.system() == "Windows":
                os.system("cls")
            elif platform.system() == "Linux":
                os.system("clear")
            menu()

        else:
            print(Colors.red+"[!] Error . Invalid option ,reloading ..")
            menu()

    menu()

except KeyboardInterrupt:
    keyboard()
