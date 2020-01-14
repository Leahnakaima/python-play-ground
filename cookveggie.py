# Leah and Nick
import json
import csv
# In a new file called cookveggies.py

#     Read vegetables.csv (see previous section) into a variable called vegetables.
with open('vegetables.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    vegetables = [dict(row) for row in rows] # Convert OrderedDict to regular dict

print(rows)


#     Print the variable vegetables.
print(vegetables)

#     Write vegetables as a JSON file called vegetables.json. It should look like this

with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f, indent = 4)
