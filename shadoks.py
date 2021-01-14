GA= chr(0x004f)
BU= chr(0x2212)
ZO= chr(0x2a3c)
MEU= chr(0x25ff)
ALPHABET_SHADOK= (GA, BU, ZO, MEU)

def entier_en_shadok(x):
    '''Permet de traduire un entier en code shadok'''
    result= ''
    if x<=3:
        return ALPHABET_SHADOK[x]
    else:
        while x>3:
            y= x%4
            result= ALPHABET_SHADOK[y] + result
            x= x//4
        result= ALPHABET_SHADOK[x] + result
        return result
    
def shadok_en_entier(x):
    '''Permet de traduire un code shadok en nombre entier'''
    result= 0
    y= 0
    if len(x)==1:
        for i in range(4):
            if x==ALPHABET_SHADOK[i]:
                return i
    else:
        for j in range(len(x)):
            p= x[-1-y]
            for i in range(4):
                if p==ALPHABET_SHADOK[i]:
                    puissance= 4**y
                    result= result+ i*puissance
            y= y+1
        return result

def octet_en_shadok(x):
    '''Permet de coder un nombre sur un octet en 4 caractères shadok.
    Contraintes : x doit seulement être un nombre entier de 0 à 255'''
    result= ''
    for i in range(3):
        y= x%4
        result= ALPHABET_SHADOK[y] + result
        x= x//4
    result= ALPHABET_SHADOK[x] + result
    return result

def code_car_en_shadok(car):
    '''Permet de coder un caractère ASCII en shadok.
Contrainte : Les caractères qui ne sont pas dans le dictionnaire ASCII ne sont pas traduisibles'''
    c= int(ord(car))
    result= octet_en_shadok(c)
    return result


def code_en_shadok(x):
    '''Permet de coder une chaine de caractère ASCII en shadok
Contrainte : Les caractères qui ne sont pas dans le dictionnaire ASCII ne sont pas traduisibles'''
    lettres= len(x)
    y= ""
    l=0
    for i in range(lettres):
        c= x[l]
        y= y+ code_car_en_shadok(c)
        l= l+1
    return y

def decode_car_en_shadok(c):
    '''Permet de décoder un shadok en caractère ASCII
Contrainte : Il ne doit y avoir que 4 shadok, pas plus ni moins'''
    c= shadok_en_entier(c)
    c= chr(c)
    return c
    
def decode_en_shadok(x):
    '''Permet de décoder une suite de shadoks en caractères ASCII
Contrainte : Il ne doit y avoir que des "quartet" de shadok'''
    nbr_car= int(len(x)/4)
    y= ""
    l=0
    for i in range(nbr_car):
        c= x[l:l+4]
        y= y+ decode_car_en_shadok(c)
        l= l+4
    return y