import csv


with open("billboard200.csv", encoding="utf-8") as file:
    billboard200_reader = csv.reader(file)

    header, *data = billboard200_reader

    for row in data:
        billboard_dict = {k: v for (k, v) in zip(header, row)}
        print(billboard_dict)
