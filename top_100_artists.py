import csv

with open("billboard200.csv", encoding="utf-8") as file:
    billboard200_reader = csv.reader(file)

    header, *data = billboard200_reader

    billboard_list = []
    for row in data:
        billboard_dict = {k: v for (k, v) in zip(header, row)}
        if billboard_dict["Weeks in Charts"] == "-":
            billboard_dict["Weeks in Charts"] = 0
        billboard_list.append(billboard_dict)
    print(billboard_list[0])
    # billboard_sorted = sorted(
    #     billboard_list, key=lambda x: x["Weeks in Charts"],
    #     reverse=True
    #     )
    # print("primeiro", billboard_list[0])
    # print("último", billboard_sorted[len(billboard_sorted) - 1])
    # print("sem sort", billboard_list[len(billboard_list) - 1])
    # billboard_list.sort(key=lambda x: x["Weeks in Charts"])
    # print("com sorte", billboard_list[len(billboard_list) - 1])
