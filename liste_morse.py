from operator import index


alphabet=["a",
"b","c","d","e","f","g","h","i",
"j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]

morse=[".-",
"-...",
"-.-.",
"-..",
".",
"..-.",
"--.",
"....",
"..",
".---",
"-.-",
".-..",
"--",
"-.",
"---",
".--.",
"--.-",
".-.",
"...",
"-",
"..-",
"...-",
".--",
"-..-",
"-.--",
"--..",
" "] 

def encode(lettre):
    # on cherche l'index de la lettre daans la liste alphabet
    index = alphabet.index(lettre)
    code_morse= morse[index]
    #on renvoit 
    return code_morse
#decode code morse > lettre
def decode(code):
    index =morse.index(code)
    lettre = alphabet[index]
    return lettre