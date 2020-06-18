import requests, json, time

def swstarship():
    page = 1
    id = 1
    test = []

    print("Vous consultez la base de donnée technique de l'Académie Jedi.")

    while page < 5:
            r = requests.get(f'https://swapi.dev/api/starships/?page={page}')
            response = json.loads(r.content)
            test += response.get('results')
            page +=1

    for i in range(len(test)):
        name = test[i].get('name')
        print(f'{id} : {name}')
        id +=1

    print('Choisir un vaisseau :')
    choice = int(input())
    ship = test[choice - 1]
    listValues = []
    for k,v in ship.items():
        listValues.append(v)
        if k == 'starship_class':
            break

    class starship():
        def __init__(self,list):
            self.name = listValues[0]
            self.model = listValues[1]
            self.manufacturer = listValues[2]
            self.cost_in_credits = listValues[3]
            self.length = listValues[4]
            self.max_atmosphering_speed = listValues[5]
            self.crew = listValues[6]
            self.passengers = listValues[7]
            self.cargo_capacity = listValues[8]
            self.consumables = listValues[9]
            self.hyperdrive_rating = listValues[10]
            self.MGLT = listValues[11]
            self.starship_class = listValues[12]

        def getValeur(self):
            if self.cost_in_credits == 'unknown':
                return 'inconnu.'
            else:
                return str(self.cost_in_credits) + ' crédits républicains.'
        
        def getCargo(self):
            if self.cargo_capacity == 'unknown':
                return 'inconnu.'
            else:
                return str(self.cost_in_credits) + ' kg.'


    choiceShip = starship(listValues)

    print(f'Chargement des informations de {choiceShip.name}.')
    for i in range(5):
        print('.',end='',flush=True)
        time.sleep(0.5)
    print()
    print(f'''
    Nom du vaisseau : {choiceShip.name}
    Modèle : {choiceShip.model}
    Nom du constructeur : {choiceShip.manufacturer}
    Valeur : {choiceShip.getValeur()}
    Longueur du vaisseau : {choiceShip.length} mètres.
    Vitesse max. en atmopshère : {choiceShip.max_atmosphering_speed} km/h.
    Taille de l'équipage : {choiceShip.crew}
    Nombre max. de passagers : {choiceShip.passengers}
    Capacité de fret : {choiceShip.getCargo()}
    Autonomie max. : {choiceShip.consumables}
    Echelle hyperdrive : {choiceShip.hyperdrive_rating}
    Mégalumière /heure : {choiceShip.MGLT}
    Classe du vaisseau : {choiceShip.starship_class}
    ''')



        
        
