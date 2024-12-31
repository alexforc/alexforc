'''
L1 liste1 = [1, 2, 3]
L2 liste2 = ["a","b","c","d"]
L3 liste3 = [ ]
On vient de définir 3 listes dont la dernière (liste3) est une liste vide.
On peut s’assurer qu’il s’agit bien de listes grâce à la méthode type() :
Langage Python	Interprétation
L1 liste1 = [1, 2, 3]
L2 liste2 = ["a","b","c","d"]
L3 liste3 = [ ]
L4 type(liste1)
L5 <class 'list'>
L6 type(liste2)
L7 <class 'list'>
L8 type(liste3)
L9 <class 'list'>
'''

#Exemple 1
#Langage Python	Interprétation
'''L1 liste = [0 for i in range(5)]
L2 liste
L3 [0, 0, 0, 0, 0]	L1 : La commande [0 for i in range(5)] demande de créer une liste contenant 5 fois la valeur 0.
L2 et L3 : La liste demandée s’affiche.
Exemple 2
Langage Python	Interprétation
L1 liste = [i for i in range(5)]
L2 liste
L3 [0, 1, 2, 3, 4]	L1 : La commande [i for i in range(5)] demande de créer une liste contenant les 5 premiers entiers naturels.
L2 et L3 : La liste demandée s’affiche.
Exemple 3
Langage Python	Interprétation
L1 liste = [i**2 for i in range(5)]
L2 liste
L3 [0, 1, 4, 9, 16]	L1 : La commande [i**2 for i in range(5)] demande de créer une liste contenant les 5 premiers carrés.
L2 et L3 : La liste demandée s’affiche.
Si l’on veut les carrés des entiers de 1 à 4 :
L1 liste = [i**2 for i in range(1,5)]
Par rapport à l’exemple précédent, on a précisé à l’intérieur des parenthèses que le rang démarrait à 1.
L2 liste
L3 [1, 4, 9, 16]'''
