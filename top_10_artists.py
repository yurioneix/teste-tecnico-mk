import csv

with open("billboard200.csv", encoding="utf-8") as file:
    billboard200_reader = csv.reader(file)

    header, *data = billboard200_reader

billboard_list = []

for row in data:
    billboard_dict = {k: v for (k, v) in zip(header, row)}
    billboard_list.append(billboard_dict)
print(billboard_list)
