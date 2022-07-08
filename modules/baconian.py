def encrypt(word):

    if word == word.upper():

        baconian = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
            'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
            'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
            'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
            'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}
        
        encrypted = ""
        for i in range (0,len(word)):
            encrypted = encrypted + baconian[word[i]]
        return encrypted

    elif word == word.lower():
        word = word.upper()
        baconian = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
            'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
            'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
            'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
            'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}
        
        encrypted = ""
        for i in range (0,len(word)):
            encrypted = encrypted + baconian[word[i]]
        return encrypted


def decrypt(word):

    baconian = {
        'aaaaa' : "A", 'aaaaab' : 'B', 'aaaba' : "C", 'aaabb':'D', 'aabaa':'E',
        'aabab':'F', 'aabba':'G', 'aabbb':'H', 'abaaa':'I', 'abaab':'J',
        'ababa':'K', 'ababb':'L', 'abbaa' : 'L', 'abbaa':'M', 'abbab':'N', 'abbba':'O',
        'abbbb':'P', 'baaaa':'Q', 'baaab':'R', 'baaba':'S', 'baabb':'T', 'babaa':'U', 'babab':'V',
        'babba':'W', 'babbb':'X', 'bbaaa':'Y', 'bbaab':'Z'}

    decrypted = ""
    
    for i in range(0, len(word),5):
        decrypted = decrypted + baconian[word[i:i+5]]
        return decrypted


