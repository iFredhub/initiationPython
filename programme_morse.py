# importer nos librairies
# on nous affiche : entrez un caractere de a->z
# on tape une lettre
# on retrouve la position de la lettre dans alphabet
# on affiche le code de morse correspondat a l'index trouve
# le programme nous retourne les sympboles correspondants

#from tkinter import variable
from urllib import response
import liste_morse

print("entrer un mots")
mots= input(">>>")
code=""
# bonjour
#pour chaque lettre dans mots, on encode la lettre en morse
# on encode la lettre en morse
# une fois le mots encode, on l'affiche

for lettre in mots:

#on appelle notre function encode dans notre librairie et on stoque le code recupere

    code=code + liste_morse.encode(lettre)
    code = code + " "

print(code)
# on decode un code morse en mots
print("entrez un code morse")
code = input(">>>")
mots=""
#"--- -. ---"
#[---, -., ---]
# On decoupe notre code en liste de code separe par un espace
liste_code = str.split(code," ")
#on affiche le resultat de la decoupe
print(code)
# pour chaque element de la liste_code, on recupere la lettre correspondante et on 
# la stoque dans la variable mots
print(liste_code)

for element in liste_code:
    mots = mots + liste_morse.decode(element)




print(mots)