@echo off

echo import tkinter as tk >temp.py
echo from tkinter import messagebox >>temp.py

echo choix=input("Quelle application voulez vous utiliser ? 1 pour le crypteur et 2 pour le décrypteur ") >>temp.py
echo choix=str(choix) >>temp.py

echo if choix=='1': >>temp.py
echo     word=[] >>temp.py

echo     word1=input("Mettre votre phrase : ") >>temp.py
echo     word1=str(word1) >>temp.py

echo     for i in range(len(word1)): >>temp.py
echo         word.append(word1[i]) >>temp.py

echo     print('Votre mot est : ',word1) >>temp.py

echo     def crypteur(): >>temp.py
echo         wordcrypter=[] >>temp.py
echo         for i in range(len(word)): >>temp.py
echo             if word[i]=='a' or word[i]=='A': >>temp.py
echo                 wordcrypter.append('._ ') >>temp.py
echo             elif word[i]=='b' or word[i]=='B': >>temp.py
echo                 wordcrypter.append('_... ') >>temp.py
echo             elif word[i]=='c' or word[i]=='C': >>temp.py
echo                 wordcrypter.append('_._. ') >>temp.py
echo             elif word[i]=='d' or word[i]=='D': >>temp.py
echo                 wordcrypter.append('_.. ') >>temp.py
echo             elif word[i]=='e' or word[i]=='E': >>temp.py
echo                 wordcrypter.append('. ') >>temp.py
echo             elif word[i]=='f' or word[i]=='F': >>temp.py
echo                 wordcrypter.append('.._. ') >>temp.py
echo             elif word[i]=='g' or word[i]=='G': >>temp.py
echo                 wordcrypter.append('__. ') >>temp.py
echo             elif word[i]=='h' or word[i]=='H': >>temp.py
echo                 wordcrypter.append('.... ') >>temp.py
echo             elif word[i]=='i' or word[i]=='I': >>temp.py
echo                 wordcrypter.append('.. ') >>temp.py
echo             elif word[i]=='j' or word[i]=='J': >>temp.py
echo                 wordcrypter.append('.___ ') >>temp.py
echo             elif word[i]=='k' or word[i]=='K': >>temp.py
echo                 wordcrypter.append('_._ ') >>temp.py
echo             elif word[i]=='l' or word[i]=='L': >>temp.py
echo                 wordcrypter.append('._.. ') >>temp.py
echo             elif word[i]=='m' or word[i]=='M': >>temp.py
echo                 wordcrypter.append('__ ') >>temp.py
echo             elif word[i]=='n' or word[i]=='N': >>temp.py
echo                 wordcrypter.append('_. ') >>temp.py
echo             elif word[i]=='o' or word[i]=='O': >>temp.py
echo                 wordcrypter.append('___ ') >>temp.py
echo             elif word[i]=='p' or word[i]=='P': >>temp.py
echo                 wordcrypter.append('.__. ') >>temp.py
echo             elif word[i]=='q' or word[i]=='Q': >>temp.py
echo                 wordcrypter.append('__._ ') >>temp.py
echo             elif word[i]=='r' or word[i]=='R': >>temp.py
echo                 wordcrypter.append('._. ') >>temp.py
echo             elif word[i]=='s' or word[i]=='S': >>temp.py
echo                 wordcrypter.append('... ') >>temp.py
echo             elif word[i]=='t' or word[i]=='T': >>temp.py
echo                 wordcrypter.append('_ ') >>temp.py
echo             elif word[i]=='u' or word[i]=='U': >>temp.py
echo                 wordcrypter.append('.._ ') >>temp.py
echo             elif word[i]=='v' or word[i]=='V': >>temp.py
echo                 wordcrypter.append('..._ ') >>temp.py
echo             elif word[i]=='w' or word[i]=='W': >>temp.py
echo                 wordcrypter.append('.__ ') >>temp.py
echo             elif word[i]=='x' or word[i]=='X': >>temp.py
echo                 wordcrypter.append('_.._ ') >>temp.py
echo             elif word[i]=='y' or word[i]=='Y': >>temp.py
echo                 wordcrypter.append('_.__ ') >>temp.py
echo             elif word[i]=='z' or word[i]=='Z': >>temp.py
echo                 wordcrypter.append('__.. ') >>temp.py
echo             elif word[i]==' ': >>temp.py
echo                 wordcrypter.append('  ') >>temp.py
echo             elif word[i]=='0': >>temp.py
echo                 wordcrypter.append('_____ ') >>temp.py
echo             elif word[i]=='1': >>temp.py
echo                 wordcrypter.append('.____ ') >>temp.py
echo             elif word[i]=='2': >>temp.py
echo                 wordcrypter.append('..___ ') >>temp.py
echo             elif word[i]=='3': >>temp.py
echo                 wordcrypter.append('...__ ') >>temp.py
echo             elif word[i]=='4': >>temp.py
echo                 wordcrypter.append('...._ ') >>temp.py
echo             elif word[i]=='5': >>temp.py
echo                 wordcrypter.append('..... ') >>temp.py
echo             elif word[i]=='6': >>temp.py
echo                 wordcrypter.append('_.... ') >>temp.py
echo             elif word[i]=='7': >>temp.py
echo                 wordcrypter.append('__... ') >>temp.py
echo             elif word[i]=='8': >>temp.py
echo                 wordcrypter.append('___.. ') >>temp.py
echo             elif word[i]=='9': >>temp.py
echo                 wordcrypter.append('____. ') >>temp.py
echo             elif word[i]=='.': >>temp.py
echo                 wordcrypter.append('. ') >>temp.py
echo             elif word[i]==',': >>temp.py
echo                 wordcrypter.append(', ') >>temp.py
echo             elif word[i]==':': >>temp.py
echo                 wordcrypter.append(': ') >>temp.py
echo             elif word[i]=='/': >>temp.py
echo                 wordcrypter.append('/ ') >>temp.py
echo             elif word[i]==';': >>temp.py
echo                 wordcrypter.append('; ') >>temp.py
echo             elif word[i]=='?': >>temp.py
echo                 wordcrypter.append('? ') >>temp.py
echo             elif word[i]=='!': >>temp.py
echo                 wordcrypter.append('! ') >>temp.py
echo             elif word[i]=='(': >>temp.py
echo                 wordcrypter.append('( ') >>temp.py
echo             elif word[i]==')': >>temp.py
echo                 wordcrypter.append(') ') >>temp.py
echo             elif word[i]=='[': >>temp.py
echo                 wordcrypter.append('[ ') >>temp.py
echo             elif word[i]==']': >>temp.py
echo                 wordcrypter.append('] ') >>temp.py
echo             else: >>temp.py
echo                 print('erreur tour',i) >>temp.py
echo         return wordcrypter >>temp.py
 
echo     wordcrypter__=crypteur() >>temp.py
echo     wordcrypter_='' >>temp.py

echo     for i in range(len(wordcrypter__)): >>temp.py
echo         wordcrypter_=wordcrypter_+wordcrypter__[i] >>temp.py

echo     print('Votre mot crypter est :',wordcrypter_) >>temp.py

echo     class Win: >>temp.py
echo         def popup(self, title="", sentence=""): >>temp.py
echo             root = tk.Tk() >>temp.py
echo             root.withdraw() >>temp.py
echo             root.lift() >>temp.py
echo             root.attributes('-topmost', True) >>temp.py
echo             messagebox.showinfo(title=title, message=sentence, parent=root) >>temp.py
echo             root.destroy() >>temp.py

echo     win=Win() >>temp.py
echo     win.popup("Morse crypté", f"Le morse crypté : {wordcrypter_}") >>temp.py

echo elif choix=='2': >>temp.py
echo     wordcrypter=[] >>temp.py

echo     wordcrypter1=input("Mettez votre code morse avec un espace entre chaque lettres sans ponctuation : ") >>temp.py
echo     wordcrypter1=str(wordcrypter1) >>temp.py

echo     print('Votre mot est : ',wordcrypter1) >>temp.py

echo     for i in range(len(wordcrypter1)): >>temp.py
echo         wordcrypter.append(wordcrypter1[i]) >>temp.py

echo     lengh=len(wordcrypter) >>temp.py

echo     def decrypteur(): >>temp.py
echo         word=[] >>temp.py
echo         i=0 >>temp.py
echo         while i ^< lengh: >>temp.py
echo             if wordcrypter[i:i+3]==['.', '_', ' ']: >>temp.py
echo                 word.append('a') >>temp.py
echo                 i=i+3 >>temp.py
echo             elif wordcrypter[i:i+5]==['_', '.', '.', '.', ' ']: >>temp.py
echo                 word.append('b') >>temp.py
echo                 i=i+5 >>temp.py
echo             elif wordcrypter[i:i+5]==['_', '.', '_', '.', ' ']: >>temp.py
echo                 word.append('c') >>temp.py
echo                 i=i+5 >>temp.py
echo             elif wordcrypter[i:i+4]==['_', '.', '.', ' ']: >>temp.py
echo                 word.append('d') >>temp.py
echo                 i=i+4 >>temp.py
echo             elif wordcrypter[i:i+2]==['.', ' ']: >>temp.py
echo                 word.append('e') >>temp.py
echo                 i=i+2 >>temp.py
echo             elif wordcrypter[i:i+5]==['.', '.', '_', '.', ' ']: >>temp.py
echo                 word.append('f') >>temp.py
echo                 i=i+5 >>temp.py
echo             elif wordcrypter[i:i+4]==['_', '_', '.', ' ']: >>temp.py
echo                 word.append('g') >>temp.py
echo                 i=i+4 >>temp.py
echo             elif wordcrypter[i:i+5]==['.', '.', '.', '.', ' ']: >>temp.py
echo                 word.append('h') >>temp.py
echo                 i=i+5 >>temp.py
echo             elif wordcrypter[i:i+3]==['.', '.', ' ']: >>temp.py
echo                 word.append('i') >>temp.py
echo                 i=i+3 >>temp.py
echo             elif wordcrypter[i:i+5]==['.', '_', '_', '_', ' ']: >>temp.py
echo                 word.append('j') >>temp.py
echo                 i=i+5 >>temp.py
echo             elif wordcrypter[i:i+4]==['_', '.', '_', ' ']: >>temp.py
echo                 word.append('k') >>temp.py
echo                 i=i+4 >>temp.py
echo             elif wordcrypter[i:i+5]==['.', '_', '.', '.', ' ']: >>temp.py
echo                 word.append('l') >>temp.py
echo                 i=i+5 >>temp.py
echo             elif wordcrypter[i:i+3]==['_', '_', ' ']: >>temp.py
echo                 word.append('m') >>temp.py
echo                 i=i+3 >>temp.py
echo             elif wordcrypter[i:i+3]==['_', '.', ' ']: >>temp.py
echo                 word.append('n') >>temp.py
echo                 i=i+3 >>temp.py
echo             elif wordcrypter[i:i+4]==['_', '_', '_', ' ']: >>temp.py
echo                 word.append('o') >>temp.py
echo                 i=i+4 >>temp.py
echo             elif wordcrypter[i:i+5]==['.', '_', '_', '.', ' ']: >>temp.py
echo                 word.append('p') >>temp.py
echo                 i=i+5 >>temp.py
echo             elif wordcrypter[i:i+5]==['_', '_', '.', '_', ' ']: >>temp.py
echo                 word.append('q') >>temp.py
echo                 i=i+5 >>temp.py
echo             elif wordcrypter[i:i+4]==['.', '_', '.', ' ']: >>temp.py
echo                 word.append('r') >>temp.py
echo                 i=i+4 >>temp.py
echo             elif wordcrypter[i:i+4]==['.', '.', '.', ' ']: >>temp.py
echo                 word.append('s') >>temp.py
echo                 i=i+4 >>temp.py
echo             elif wordcrypter[i:i+2]==['_', ' ']: >>temp.py
echo                 word.append('t') >>temp.py
echo                 i=i+2 >>temp.py
echo             elif wordcrypter[i:i+4]==['.', '.', '_', ' ']: >>temp.py
echo                 word.append('u') >>temp.py
echo                 i=i+4 >>temp.py
echo             elif wordcrypter[i:i+5]==['.', '.', '.', '_', ' ']: >>temp.py
echo                 word.append('v') >>temp.py
echo                 i=i+5 >>temp.py
echo             elif wordcrypter[i:i+4]==['.', '_', '_', ' ']: >>temp.py
echo                 word.append('w') >>temp.py
echo                 i=i+4 >>temp.py
echo             elif wordcrypter[i:i+5]==['_', '.', '.', '_', ' ']: >>temp.py
echo                 word.append('x') >>temp.py
echo                 i=i+5 >>temp.py
echo             elif wordcrypter[i:i+5]==['_', '.', '_', '_', ' ']: >>temp.py
echo                 word.append('y') >>temp.py
echo                 i=i+5 >>temp.py
echo             elif wordcrypter[i:i+5]==['_', '_', '.', '.', ' ']: >>temp.py
echo                 word.append('z') >>temp.py
echo                 i=i+5 >>temp.py
echo             elif wordcrypter[i:i+2]==[' ', ' ']: >>temp.py
echo                 word.append(' ') >>temp.py
echo                 i=i+2 >>temp.py
echo             elif wordcrypter[i:i+6]==['_', '_', '_', '_', '_', ' ']: >>temp.py
echo                 word.append('0') >>temp.py
echo                 i=i+6 >>temp.py
echo             elif wordcrypter[i:i+6]==['.', '_', '_', '_', '_', ' ']: >>temp.py
echo                 word.append('1') >>temp.py
echo                 i=i+6 >>temp.py
echo             elif wordcrypter[i:i+6]==['.', '.', '_', '_', '_', ' ']: >>temp.py
echo                 word.append('2') >>temp.py
echo                 i=i+6 >>temp.py
echo             elif wordcrypter[i:i+6]==['.', '.', '.', '_', '_', ' ']: >>temp.py
echo                 word.append('3') >>temp.py
echo                 i=i+6 >>temp.py
echo             elif wordcrypter[i:i+6]==['.', '.', '.', '.', '_', ' ']: >>temp.py
echo                 word.append('4') >>temp.py
echo                 i=i+6 >>temp.py
echo             elif wordcrypter[i:i+6]==['.', '.', '.', '.', '.', ' ']: >>temp.py
echo                 word.append('5') >>temp.py
echo                 i=i+6 >>temp.py
echo             elif wordcrypter[i:i+6]==['_', '.', '.', '.', '.', ' ']: >>temp.py
echo                 word.append('6') >>temp.py
echo                 i=i+6 >>temp.py
echo             elif wordcrypter[i:i+6]==['_', '_', '.', '.', '.', ' ']: >>temp.py
echo                 word.append('7') >>temp.py
echo                 i=i+6 >>temp.py
echo             elif wordcrypter[i:i+6]==['_', '_', '_', '.', '.', ' ']: >>temp.py
echo                 word.append('8') >>temp.py
echo                 i=i+6 >>temp.py
echo             elif wordcrypter[i:i+6]==['_', '_', '_', '_', '.', ' ']: >>temp.py
echo                 word.append('9') >>temp.py
echo                 i=i+6 >>temp.py
echo             else: >>temp.py
echo                 print('erreur tour',i) >>temp.py
echo                 i=i+1 >>temp.py
echo         return word >>temp.py

echo     word__=decrypteur() >>temp.py
echo     word_='' >>temp.py

echo     for i in range(len(word__)): >>temp.py
echo         word_=word_+word__[i] >>temp.py


echo     print('Votre mot décrypter est : ',word_) >>temp.py

echo     class Win: >>temp.py
echo         def popup(self, title="", sentence=""): >>temp.py
echo             root = tk.Tk() >>temp.py
echo             root.withdraw() >>temp.py
echo             root.lift() >>temp.py
echo             root.attributes('-topmost', True) >>temp.py
echo             messagebox.showinfo(title=title, message=sentence, parent=root) >>temp.py
echo             root.destroy() >>temp.py

echo     win=Win() >>temp.py
echo     win.popup("Morse décrypté", f"Le morse décrypté : {word_}") >>temp.py

echo else: >>temp.py
echo     print('Erreur sur le choix. Choix possibles 1 ou 2.') >>temp.py

echo     class Win: >>temp.py
echo         def popup(self, title="", sentence=""): >>temp.py
echo             root = tk.Tk() >>temp.py
echo             root.withdraw() >>temp.py
echo             root.lift() >>temp.py
echo             root.attributes('-topmost', True) >>temp.py
echo             messagebox.showinfo(title=title, message=sentence, parent=root) >>temp.py
echo             root.destroy() >>temp.py

echo     win=Win() >>temp.py
echo     win.popup("Erreur", "Erreur sur le choix. Choix possibles 1 ou 2.") >>temp.py


timeout /t 5 /nobreak > nul
python "temp.py" 

timeout /t 5 /nobreak > nul 
del temp.py 

exit
