import requests, json, time

def planetInfo():
    print('''
    Bienvenue dans le registre galactique de l'Académie Jedi !
    ''')

    page = 1
    id = 1
    idList = []
    choice = ''

    while page < 6:
        r = requests.get(f'https://swapi.dev/api/planets/?page={page}')
        response = json.loads(r.content)
        results = response.get('results')
        page +=1

        for i in range(len(results)):
            name = (results[i].get('name'))
            print(f'{id} : {name}')
            idList.append(id)
            id+=1

    while choice not in idList:
        print('Quelle planète voulez vous consulter ?')
        try:    
            choice = int(input())
            if choice not in idList:
                print('Saisie non reconnue.')
        except ValueError:
            print('Saisie non reconnue.')

    r = requests.get(f'https://swapi.dev/api/planets/{choice}')
    response = json.loads(r.content)

    class planet:
        def __init__(self,list):
            self.name = list[0]
            self.rotation_period = list[1] 
            self.orbital_period = list[2]
            self.diameter = list[3]
            self.climate = list[4]
            self.gravity = list[5]
            self.terrain = list[6]
            self.surface_water = list[7]
            self.population = list[8]

    listValues = []
    for k,v in response.items():
        listValues.append(v)
        if k == 'population':
            break

    planetChoice = planet(listValues)
    print(f'Chargement des informations de {planetChoice.name}.')
    for i in range(5):
        print('.',end='',flush=True)
        time.sleep(0.5)
    print()
    print(f'''
    Nom de la planète : {planetChoice.name}.
    Rotation en : {planetChoice.rotation_period} heures.
    Orbite en : {planetChoice.orbital_period} jours.
    Diamètre : {planetChoice.diameter} kilomètres.
    Climat : {planetChoice.climate}.
    Gravité : {planetChoice.gravity}.
    Terrain : {planetChoice.terrain}.
    Surface en eau : {planetChoice.surface_water} %.
    Population : {planetChoice.population} habitants.
    ''' )