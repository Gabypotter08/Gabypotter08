# Created by Gabypotter08 in Python 3.7 
# Coding utf-8

import tkinter as tk
from tkinter import messagebox

choix=input("What app do you want to use? 1 to encrypt and 2 to decrypt ")
choix=str(choix)

if choix=='1':
    word=[]

    word1=input("Your sentence: ")
    word1=str(word1)

    for i in range(len(word1)):
        word.append(word1[i])

    print('Your word is: ',word1)

    def crypteur():
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

    wordcrypter__=crypteur()
    wordcrypter_=''

    for i in range(len(wordcrypter__)):
        wordcrypter_=wordcrypter_+wordcrypter__[i]

    print('Your word encrypt is: ',wordcrypter_)

    class Win:
        def popup(self, title="", sentence=""):
            root = tk.Tk()
            root.withdraw()
            root.lift()
            root.attributes('-topmost', True)
            messagebox.showinfo(title=title, message=sentence, parent=root)
            root.destroy()

    win=Win()
    win.popup("Morse crypté", f"The encrypt morse is: {wordcrypter_}")

elif choix=='2':
    wordcrypter=[]

    wordcrypter1=input("Put your morse code with a space between each letters and without punctuation: ")
    wordcrypter1=str(wordcrypter1)

    print('Your word is: ',wordcrypter1)

    for i in range(len(wordcrypter1)):
        wordcrypter.append(wordcrypter1[i])

    lengh=len(wordcrypter)

    def decrypteur():
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

    word__=decrypteur()
    word_=''

    for i in range(len(word__)):
        word_=word_+word__[i]


    print('Your word decrypt is: ',word_)

    class Win:
        def popup(self, title="", sentence=""):
            root = tk.Tk()
            root.withdraw()
            root.lift()
            root.attributes('-topmost', True)
            messagebox.showinfo(title=title, message=sentence, parent=root)
            root.destroy()

    win=Win()
    win.popup("Morse décrypté", f"The decrypt word is: {word_}")

else:
    print('Error on the choice. Possible input : 1 and 2')

    class Win:
        def popup(self, title="", sentence=""):
            root = tk.Tk()
            root.withdraw()
            root.lift()
            root.attributes('-topmost', True)
            messagebox.showinfo(title=title, message=sentence, parent=root)
            root.destroy()

    win=Win()
    win.popup("Error", "Error on the choice. Possible input : 1 and 2")
