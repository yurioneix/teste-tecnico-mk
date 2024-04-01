import csv

with open("billboard200.csv", encoding="utf-8") as file:
    billboard200_reader = csv.reader(file)

    header, *data = billboard200_reader

billboard_list = []
for row in data:
    billboard_dict = {k: v for (k, v) in zip(header, row)}
    billboard_dict.pop("Date")
    billboard_dict.pop("Image URL")
    billboard_dict.pop("Last Week")
    if billboard_dict["Weeks in Charts"] == "-":
        billboard_dict["Weeks in Charts"] = 0
    billboard_dict["Weeks in Charts"] = int(billboard_dict["Weeks in Charts"])
    billboard_list.append(billboard_dict)
billboard_sorted = sorted(
    billboard_list, key=lambda x: x["Weeks in Charts"], reverse=True
)

keys = billboard_sorted[0].keys()

with open("top100faixas.csv", "w", encoding="utf-8") as top_100:
    dict_writer = csv.DictWriter(top_100, keys)

    headers = ["Rank", "Song", "Artist", "Peak Position", "Weeks in Charts"]
    dict_writer.writeheader()
    dict_writer.writerows(billboard_sorted[0:100])
    # for dict in billboard_sorted:
    #     for key, value in dict.items():

# desired_order_list = [
#     "Rank",
#     "Song",
#     "Artist",
#     "Peak Position",
#     "Weeks in Charts"
#     ]
# reordered_list = []
# for row in billboard_sorted:
#     reordered_dict = {k: billboard_sorted[k] for k in desired_order_list}
#     reordered_list.append(reordered_dict)
# print(billboard_sorted[0:100])
# print("primeiro", billboard_sorted[0])
# print("último", billboard_sorted[len(billboard_sorted) - 1])
