Regex_Pattern = r'(t|r|s|k|fe)$'	# Do not delete 'r'.
# Tutti i termini della prima lista finiscono per t, oppure r, oppure s, oppure k oppure fe
# mentre nessun termine della seconda lista finisce per t oppure r, oppure s, oppure k, oppure fe
# un ragionamento similare si sarebbe potuto fare per l'inizio delle parole della prima e seconda lista
# ma in questo caso (probabilmente) si complicava la gestione perchè per esempio book nella prima lista
# e boombox (nella seconda) hanno i primi tre caratteri "boo" uguali e quindi si sarebbe dovuta pensare 
# una regoletta che slitta in qual caso fino al quarto carattere. 
 
import re
T=int(input())
for i in range(T):
    print(str(bool(re.search(Regex_Pattern, input()))).lower())
    if len(Regex_Pattern) == 0:
	    print("Warning : Empty regular expression.")
    if len(Regex_Pattern) > 25:
	    print("Warning : Length of regular expression greater than 25 characters.")
