import csv

# Abre arquivo csv e desempacota os dados
with open("billboard200.csv", encoding="utf-8") as file:
    billboard200_reader = csv.reader(file)

    header, *data = billboard200_reader

# Cria uma lista vazia para armazenar os dados em formato de dicionário
billboard_list = []

for row in data:
    # Transformo em dicionário
    billboard_dict = {k: v for (k, v) in zip(header, row)}

    # Removo as chaves que não serão utilizadas
    billboard_dict.pop("Date")
    billboard_dict.pop("Image URL")
    billboard_dict.pop("Last Week")

    # Transformo Weeks in Charts com hífen para 0 e transformo o tipo de dado da chave Weeks in Charts para int.
    if billboard_dict["Weeks in Charts"] == "-":
        billboard_dict["Weeks in Charts"] = 0
    billboard_dict["Weeks in Charts"] = int(billboard_dict["Weeks in Charts"])

    # Adiciono os dicionários na lista
    billboard_list.append(billboard_dict)

# Ordena a lista de dicionários por semanas em ordem decrescente.
billboard_sorted = sorted(
    billboard_list, key=lambda x: x["Weeks in Charts"], reverse=True
)

# Obtém as chaves dos dicionários da lista ordenada.
keys = billboard_sorted[0].keys()

# Cria um arquivo csv com os dados ordenados.
with open("top100faixas.csv", "w", encoding="utf-8") as top_100:
    # Cria um objeto DictWriter para escrever os dados em um arquivo csv.
    dict_writer = csv.DictWriter(top_100, keys)

    # Escreve o cabeçalho do arquivo csv.
    headers = ["Rank", "Song", "Artist", "Peak Position", "Weeks in Charts"]

    dict_writer.writeheader()
    # Escreve os dados ordenados no arquivo csv.
    dict_writer.writerows(billboard_sorted[0:100])