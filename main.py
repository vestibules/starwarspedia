import characters, planets,starships

encyclo = True

def mainMenu():
    choice = ''
    menu = {'1' : 'Planètes', '2' : 'Personnages', '3' : 'Vaisseaux'}
    print('Voici la liste des éléments consultables dans cette encyclopédie :')
    for k,v in menu.items():
        print(f'{k} : {v}')
    while choice not in menu.keys():
        print('Sélectionner la section souhaitée :')
        choice = input()
        if choice == '1':
            planets.planetInfo()
        elif choice == '2':
            characters.swchar()
        elif choice == '3':
            starships.swstarship()
        else:
            print('Sélection inconnue.')

def replay():
    choice = ''
    while choice.lower() != 'o' or choice != 'n':
        print('Souhaitez vous faire une autre recherche ? o/n')
        choice = input()
        if choice == 'o':
            return True
        elif choice == 'n':
            print("Fermeture de l'encyclopédie ...")
            return False
        else:
            print('Sélection inconnue')

while encyclo:
    mainMenu()
    encyclo = replay()
