#By Leah Nakaima and Nick Anway
vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]


#Loops through each vegetable
#In the loop, write the name of each vegetable and the color into a CSV called vegetables.csv

import csv

with open('vegetables.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color', 'length'])
	for x in vegetables:
		name = x["name"]
		color = x["color"]
		length = len(name)
		writer.writerow([name, color, length])


