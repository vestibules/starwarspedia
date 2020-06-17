import characters, planets

encyclo = True

def mainMenu():
    menu = {'1' : 'Planètes', '2' : 'Personnages'}
    print('Voici la liste des éléments consultables dans cette encyclopédie :')
    for k,v in menu.items():
        print(f'{k} : {v}')
    choice = input()
    if choice == '1':
        planets.planetInfo()
    elif choice == '2':
        characters.swchar()

def replay():
    print('Souhaitez vous faire une autre recherche ? o/n')
    choice = input()
    if choice == 'o':
        return True
    elif choice == 'n':
        return False

while encyclo:
    mainMenu()
    encyclo = replay()
