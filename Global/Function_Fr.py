# Created by Gabypotter08, the 11/02/2025 in Python 3.7
# Coding utf-8

from random import *

def caesar(sentance:str, deplacement:int=1):
  """
  crypte la phrase avec un déplacement : deplacement
  """
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  min=[]
  phrase_caesar=''

  for i in range(len(phrase)):
      if phrase[i]==' ':
          phrase_caesar=phrase_caesar+' '
      else:
          phrase_caesar=phrase_caesar + alphabet[alphabet.index(phrase[i])+deplacement]
  return phrase_caesar


def celsius(valeur_fahrenheit:int=0) -> float:
    """
    convertir fahrenheit en celsius
    """
    valeur_celsius=(valeur_fahrenheit-32)*5/9
    return valeur_celsius

def fahrenheit(valeur_celsius:int=0)->float:
    """
    convertir celsius en fahrenheit
    """
    valeur_fahrenheit=(valeur_celsius* 9/5) + 32 
    return valeur_fahrenheit

def miles(valeur_km:int=0)-> float:
    """
    convertir kilomètres en miles
    """
    valeur_miles=valeur_km/1,609
    return valeur_miles

def km(valeur_miles:int=0)-> float:
    """
    convertir miles en kilomètres
    """
    valeur_km=valeur_miles*1,609
    return valeur_km

def tri_ok(liste:list, c:bool=True)->bool:
    """
    Renvoie True si la liste est triée par ordre croissant
    Si c==False: renvoie True si la liste est triée par ordre décroissant
    La fonction peut aussi vérifier si un str est par ordre alphabétique
    """
    if c:
        for i in range(len(liste)-1):
            if liste[i+1]<liste[i]:
                return False
    else: 
        for i in range(len(liste)-1):
            if liste[i+1]>liste[i]:
                return False
    return True

def crypteur(word:str):
    """
    Crypte le mot et la phrase insérer vers le morse
    """
    wordcrypter=[]
    for i in range(len(word)):
        if word[i]=='a' or word[i]=='A':
            wordcrypter.append('._ ')
        elif word[i]=='b' or word[i]=='B':
            wordcrypter.append('_... ')
        elif word[i]=='c' or word[i]=='C':
            wordcrypter.append('_._. ')
        elif word[i]=='d' or word[i]=='D':
            wordcrypter.append('_.. ')
        elif word[i]=='e' or word[i]=='E':
            wordcrypter.append('. ')
        elif word[i]=='f' or word[i]=='F':
            wordcrypter.append('.._. ')
        elif word[i]=='g' or word[i]=='G':
            wordcrypter.append('__. ')
        elif word[i]=='h' or word[i]=='H':
            wordcrypter.append('.... ')
        elif word[i]=='i' or word[i]=='I':
            wordcrypter.append('.. ')
        elif word[i]=='j' or word[i]=='J':
            wordcrypter.append('.___ ')
        elif word[i]=='k' or word[i]=='K':
            wordcrypter.append('_._ ')
        elif word[i]=='l' or word[i]=='L':
            wordcrypter.append('._.. ')
        elif word[i]=='m' or word[i]=='M':
            wordcrypter.append('__ ')
        elif word[i]=='n' or word[i]=='N':
            wordcrypter.append('_. ')
        elif word[i]=='o' or word[i]=='O':
            wordcrypter.append('___ ')
        elif word[i]=='p' or word[i]=='P':
            wordcrypter.append('.__. ')
        elif word[i]=='q' or word[i]=='Q':
            wordcrypter.append('__._ ')
        elif word[i]=='r' or word[i]=='R':
            wordcrypter.append('._. ')
        elif word[i]=='s' or word[i]=='S':
            wordcrypter.append('... ')
        elif word[i]=='t' or word[i]=='T':
            wordcrypter.append('_ ')
        elif word[i]=='u' or word[i]=='U':
            wordcrypter.append('.._ ')
        elif word[i]=='v' or word[i]=='V':
            wordcrypter.append('..._ ')
        elif word[i]=='w' or word[i]=='W':
            wordcrypter.append('.__ ')
        elif word[i]=='x' or word[i]=='X':
            wordcrypter.append('_.._ ')
        elif word[i]=='y' or word[i]=='Y':
            wordcrypter.append('_.__ ')
        elif word[i]=='z' or word[i]=='Z':
            wordcrypter.append('__.. ')
        elif word[i]==' ':
            wordcrypter.append('  ')
        elif word[i]=='0':
            wordcrypter.append('_____ ')
        elif word[i]=='1':
            wordcrypter.append('.____ ')
        elif word[i]=='2':
            wordcrypter.append('..___ ')
        elif word[i]=='3':
            wordcrypter.append('...__ ')
        elif word[i]=='4':
            wordcrypter.append('...._ ')
        elif word[i]=='5':
            wordcrypter.append('..... ')
        elif word[i]=='6':
            wordcrypter.append('_.... ')
        elif word[i]=='7':
            wordcrypter.append('__... ')
        elif word[i]=='8':
            wordcrypter.append('___.. ')
        elif word[i]=='9':
            wordcrypter.append('____. ')
        elif word[i]=='.':
            wordcrypter.append('. ')
        elif word[i]==',':
            wordcrypter.append(', ')
        elif word[i]==':':
            wordcrypter.append(': ')
        elif word[i]=='/':
            wordcrypter.append('/ ')
        elif word[i]==';':
            wordcrypter.append('; ')
        elif word[i]=='?':
            wordcrypter.append('? ')
        elif word[i]=='!':
            wordcrypter.append('! ')
        elif word[i]=='(':
            wordcrypter.append('( ')
        elif word[i]==')':
            wordcrypter.append(') ')
        elif word[i]=='[':
            wordcrypter.append('[ ')
        elif word[i]==']':
            wordcrypter.append('] ')
        else:
            print('erreur tour',i)
    return wordcrypter

    
  def decrypteur():
      """
      Décrypte le mot ou la phrase du morse vers le lisible
      """
      word=[]
      i=0
      while i < lengh:
          if wordcrypter[i:i+3]==['.', '_', ' ']:
              word.append('a')
              i=i+3
          elif wordcrypter[i:i+5]==['_', '.', '.', '.', ' ']:
              word.append('b')
              i=i+5
          elif wordcrypter[i:i+5]==['_', '.', '_', '.', ' ']:
              word.append('c')
              i=i+5
          elif wordcrypter[i:i+4]==['_', '.', '.', ' ']:
              word.append('d')
              i=i+4
          elif wordcrypter[i:i+2]==['.', ' ']:
              word.append('e')
              i=i+2
          elif wordcrypter[i:i+5]==['.', '.', '_', '.', ' ']:
              word.append('f')
              i=i+5
          elif wordcrypter[i:i+4]==['_', '_', '.', ' ']:
              word.append('g')
              i=i+4
          elif wordcrypter[i:i+5]==['.', '.', '.', '.', ' ']:
              word.append('h')
              i=i+5
          elif wordcrypter[i:i+3]==['.', '.', ' ']:
              word.append('i')
              i=i+3
          elif wordcrypter[i:i+5]==['.', '_', '_', '_', ' ']:
              word.append('j')
              i=i+5
          elif wordcrypter[i:i+4]==['_', '.', '_', ' ']:
              word.append('k')
              i=i+4
          elif wordcrypter[i:i+5]==['.', '_', '.', '.', ' ']:
              word.append('l')
              i=i+5
          elif wordcrypter[i:i+3]==['_', '_', ' ']:
              word.append('m')
              i=i+3
          elif wordcrypter[i:i+3]==['_', '.', ' ']:
              word.append('n')
              i=i+3
          elif wordcrypter[i:i+4]==['_', '_', '_', ' ']:
              word.append('o')
              i=i+4
          elif wordcrypter[i:i+5]==['.', '_', '_', '.', ' ']:
              word.append('p')
              i=i+5
          elif wordcrypter[i:i+5]==['_', '_', '.', '_', ' ']:
              word.append('q')
              i=i+5
          elif wordcrypter[i:i+4]==['.', '_', '.', ' ']:
              word.append('r')
              i=i+4
          elif wordcrypter[i:i+4]==['.', '.', '.', ' ']:
              word.append('s')
              i=i+4
          elif wordcrypter[i:i+2]==['_', ' ']:
              word.append('t')
              i=i+2
          elif wordcrypter[i:i+4]==['.', '.', '_', ' ']:
              word.append('u')
              i=i+4
          elif wordcrypter[i:i+5]==['.', '.', '.', '_', ' ']:
              word.append('v')
              i=i+5
          elif wordcrypter[i:i+4]==['.', '_', '_', ' ']:
              word.append('w')
              i=i+4
          elif wordcrypter[i:i+5]==['_', '.', '.', '_', ' ']:
              word.append('x')
              i=i+5
          elif wordcrypter[i:i+5]==['_', '.', '_', '_', ' ']:
              word.append('y')
              i=i+5
          elif wordcrypter[i:i+5]==['_', '_', '.', '.', ' ']:
              word.append('z')
              i=i+5
          elif wordcrypter[i:i+2]==[' ', ' ']:
              word.append(' ')
              i=i+2
          elif wordcrypter[i:i+6]==['_', '_', '_', '_', '_', ' ']:
              word.append('0')
              i=i+6
          elif wordcrypter[i:i+6]==['.', '_', '_', '_', '_', ' ']:
              word.append('1')
              i=i+6
          elif wordcrypter[i:i+6]==['.', '.', '_', '_', '_', ' ']:
              word.append('2')
              i=i+6
          elif wordcrypter[i:i+6]==['.', '.', '.', '_', '_', ' ']:
              word.append('3')
              i=i+6
          elif wordcrypter[i:i+6]==['.', '.', '.', '.', '_', ' ']:
              word.append('4')
              i=i+6
          elif wordcrypter[i:i+6]==['.', '.', '.', '.', '.', ' ']:
              word.append('5')
              i=i+6
          elif wordcrypter[i:i+6]==['_', '.', '.', '.', '.', ' ']:
              word.append('6')
              i=i+6
          elif wordcrypter[i:i+6]==['_', '_', '.', '.', '.', ' ']:
              word.append('7')
              i=i+6
          elif wordcrypter[i:i+6]==['_', '_', '_', '.', '.', ' ']:
              word.append('8')
              i=i+6
          elif wordcrypter[i:i+6]==['_', '_', '_', '_', '.', ' ']:
              word.append('9')
              i=i+6
          else:
              print('erreur tour',i)
              i=i+1
      return word



def dice(nbr_faces:int=6, nbr_lance:int = 1): 
    """
    fonction qui simule un lancé de dé
    """
    liste_result=[] 
    for i in range(nbr_lance): 
        liste_result.append(randint(1, nbr_faces)) 
    return liste_result 

def mot_de_passe(nbr_tour:int=1)->str:
    """
    Donne un mot de passe aléatoire
    """
    alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVQWXYZ0123456789?,.;/:§!%ù¨^£$µ*+=°)àç_è-("é&)'
    mdp=''
    for i in range(nbr_tour):
        for i in range(randint(0,3)):
            mdp=mdp+alphabet[randint(0,92)]
    return mdp
