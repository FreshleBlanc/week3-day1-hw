# from IPython.display import Image
import requests

class Pokemon():
    def __init__(self, name):
        self.abilities = []
        self.name = name
        self.types = []
        self.weight = None
        self.height = None
        self.sprite = None
        self.poke_api_call()
        
    def poke_api_call(self):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')

        if response.status_code == 200:
            data = response.json()
        else:
            return 'Error'
        
        print(data)
        ability_names = [item['ability']['name'] for item in data['abilities']]
        
        self.types = data['types']
        self.abilities = ability_names
        self.weight = data['weight']
        self.height = data['height']
        self.sprite = data['sprites']['front_default']

    def lookup_pokemon(self):
        pokemon = input('What pokemon do you want to select?')
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
        
        data = response.json()
        
        
        
    def pokemon_pic(self):
        pokemon = input('What pokemon do you want to select?')
        print('self.sprite')
        print(self.sprite)
        # display(Image(self.sprite, width = 300))
        

pikachu = Pokemon('pikachu')


