import json, requests, time

def episodeOpening():

    r = requests.get('https://swapi.dev/api/films/')
    response = json.loads(r.content)
    results = response.get('results')

    print("Cette section permet d'afficher le texte d'ouverture de chaque film.")
    print('Liste des films disponibles : ')
    print()

    dicFilm = {}
    for i in range(len(results)):
        title = results[i].get('title')
        id = results[i].get('episode_id')
        dicFilm.setdefault(id,title)
    for k,v in dicFilm.items():
        print(f'{k} : {v}')

    episodeSwitcher = {'4' : '1', '5' : '2', '6' : '3', '1' : '4', '2' : '5', '3' : '6'}

    choice = ''
    while choice not in episodeSwitcher:
        print()
        print('Sélectionner un film :')
        choice = input()

        if choice in episodeSwitcher:
            choiceEpisode = episodeSwitcher.get(choice)
        else:
            print('Sélection non reconnue.')

    r = requests.get(f'https://swapi.dev/api/films/{choiceEpisode}/')
    response = json.loads(r.content)
    opening = response.get('opening_crawl')
    name = response.get('title')
    episode = response.get('episode_id')

    splited = opening.split('\r\n')

    print(f'Star Wars : Episode {episode}'.upper().center(125))
    time.sleep(0.5)
    print(f'{name}'.upper().center(125))
    print()
    time.sleep(0.5)
    for line in splited:
        print(line.center(125))
        time.sleep(0.5)