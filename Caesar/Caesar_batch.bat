@echo off

echo alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] >temp.py

echo min=[] >>temp.py

echo phrase=input("Phrase à crypter : ") >>temp.py
echo phrase_caesar='' >>temp.py
echo lettre_indiciel='' >>temp.py
echo phrase_indiciel='' >>temp.py

echo deplacement=input("Avec combien de caractères de différence voulez vous crypter votre code morse ? Attention pas plus de 26 caractères ! ") >>temp.py
echo deplacement=int(deplacement) >>temp.py

echo for i in range(len(phrase)): >>temp.py
echo     if phrase[i]==' ': >>temp.py
echo         phrase_caesar=phrase_caesar+'i' >>temp.py
echo     else: >>temp.py
echo         phrase_caesar=phrase_caesar+ alphabet[alphabet.index(phrase[i])+deplacement] >>temp.py

echo print(phrase_caesar) >>temp.py


timeout /t 5 /nobreak > nul
python "temp.py" 

timeout /t 5 /nobreak > nul 
del temp.py 

pause
