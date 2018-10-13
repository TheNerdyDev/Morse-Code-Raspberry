#coding:utf-8
#Author: Arthur Freeman.
#This program converts strings to morse code.
#And turns on and off a led to communicate the message in real life.
from gpiozero import LED #NB: Pin S1 must be connected to 3rd GPIO pin.
from time import sleep   #And pin G must be connected to ground.
print('Ce programme fait clignoter une led en convertissant un mot donné en morse et en l\'affichant dans la console et en vrai vie.')

#Array containing the alphabet in morse.
morseCode =['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
'..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
'--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
'-.--', '--..']

#Array containing the normal alphabet.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z']

mot = input('Quel mot?: ').lower() #We take an input (user word)

if type(mot) != str: #Si ce n'est pas un string, on arrête le programme.
    print('Ce n\'est pas un mot!')
    exit()

numberArray = [] #Array qui contiendra les positions du mot donné dans l'alphabet.

for i in range(0, len(mot)): #On boucle sur le mot.
    for k in range(0, len(alphabet)): #On boucle sur l'alphabet.
        if alphabet[k] == mot[i]: #Si on a un mot qui est dans l'alphabet.
            numberArray.append(k) #On l'ajoute au tableau.

morseArray = [] #Tableau qui contient les mots en morse.

for o in range(0, len(numberArray)): #On parcourt les indexs.
    print(morseCode[numberArray[o]] + ' ', end='') #On affiche la case correspondante en morse, sur la même ligne.
    morseArray.append(morseCode[numberArray[o]]) #On ajoute les strings de morse au tableau de morse.


led = LED(2) #On configure la variable qui gère notre led.
for p in range(0, len(morseArray)): #On boucle sur le tableau de morse.
    led.off() #On fait une pause de 4 secondes entre chaque lettre.
    sleep(4)
    for w in range(0, len(morseArray[p])): #On boucle sur chaque string du tableau de morse.
        if morseArray[p][w] == '.': #Si le string à un certain index du tableau est égal
            led.on()                #à un point à un certain index.
            sleep(0.25) #On clignote 0.25 [s].
            led.off()
            sleep(0.25)
        elif morseArray[p][w] == '-': #Si c'est un dash, on laisse allumer 2 [s].
            led.on()
            sleep(2)
            led.off()
            sleep(0.10)
