# By Leah and Nick
import json
import csv
from pprint import pprint
# Reads superheroes.json (in this folder)

with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)

# Write a header to the CSV file

with open('superheroes.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active'])

# Loop over the members, and for each member write a row to the csv file
	members = superheroes['members']
	for hero in members:
			hero_name = hero['name']
			hero_age = hero['age']
			hero_secretIdentity = hero['secretIdentity']
			hero_powers = hero['powers']
			for power in powers:
			hero_squadName = superheroes['squadName']
			hero_homeTown = superheroes['homeTown']
			hero_formed = superheroes['formed']
			hero_secretBase = superheroes['secretBase']
			hero_active = superheroes['active']
			writer.writerow([hero_name, hero_age, hero_secretIdentity, hero_powers, hero_squadName, hero_homeTown, hero_formed, hero_secretBase, hero_active])



