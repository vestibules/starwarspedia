import requests, json, random, time

def swchar():
    print("Vous consultez le système de fichage de l'Académie Jedi.")
    page = 1
    id = 1
    diChara = {}
    while page < 10:
        r = requests.get(f'https://swapi.dev/api/people/?page={page}')
        response = json.loads(r.content)
        test = response.get('results')
        page += 1

        for i in range(len(test)):
            if id == 17:
                id = 18
            name = (test[i].get('name'))
            diChara.setdefault(id,name)
            id +=1

    for k,v in diChara.items():
        print(f'{k} : {v}.')

    class character():
        def __init__(self,list):
            self.name = list[0]
            self.height = list[1]
            self.mass = list[2]
            self.hair_color = list[3]
            self.skin_color = list[4]
            self.eye_color = list[5]
            self.birth_year = list[6]
            self.gender = list[7]

    print('Quel fichier souhaitez - vous consulter ?')
    choice = input()
    r = requests.get(f'https://swapi.dev/api/people/{choice}')
    response = json.loads(r.content)
    listValues = []

    for k,v in response.items():
        listValues.append(v)
        if k == 'gender':
            break

    characterChoice = character(listValues)
    print(f'Chargement des informations de {characterChoice.name}.')
    for i in range(5):
        print('.',end='',flush=True)
        time.sleep(0.5)
    print()
    print(f'''
    Nom du personnage : {characterChoice.name}.
    Taille du personnage : {characterChoice.height} cm.
    Poids du personnage : {characterChoice.mass} kg.
    Couleur de cheveux : {characterChoice.hair_color}.
    Couleur de peau : {characterChoice.skin_color}.
    Couleur des yeux : {characterChoice.eye_color}.
    Année de naissance : {characterChoice.birth_year}.
    Sexe du personnage : {characterChoice.gender}.
    ''')
 