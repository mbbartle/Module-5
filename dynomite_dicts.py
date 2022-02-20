# Create an empty dictionary called pokedex.
pokedex = {}
# Add the following key, value pairs to the dictionary:
#   'Venosaur': ['Grass', 'Poisen']
#   'Charizard': ['Fire', 'Flying']
#   'Blastoise': ['Water']
pokedex['Venosaur'] = ['Grass', 'Poisen']
pokedex['Charizard'] = ['Fire', 'Flying']
pokedex['Blastoise'] = ['Water']

# Remove 'Blastoise' from the dictionary.
pokedex.pop('Blastoise')
print(pokedex)