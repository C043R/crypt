green = '\033[32m'
blue = '\033[34m'

ROT18 = str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz0123456789", "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm5678901234",)
def rot18(text):
    print(blue+"[+] Rot18 : "+text.translate(ROT18))
