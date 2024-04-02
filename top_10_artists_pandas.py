import csv
import pandas as pd

with open("billboard200.csv", encoding="utf-8") as file:
    billboard200_reader = csv.reader(file)

    header, *data = billboard200_reader

# Crio uma lista vazia para armazenar os dicionários
billboard_list = []

for row in data:
    # Transformo em dicionário
    billboard_dict = {k: v for (k, v) in zip(header, row)}

    # Transformo Weeks in Charts com hífen para 0
    if billboard_dict["Weeks in Charts"] == "-":
        billboard_dict["Weeks in Charts"] = 0

    # Transformo o tipo de dado da chave Weeks in Charts para int
    billboard_dict["Weeks in Charts"] = int(billboard_dict["Weeks in Charts"])

    # Adiciono os dicionários na lista
    billboard_list.append(billboard_dict)

# Cria um dataframe a partir da lista de dicionários
df = pd.DataFrame(billboard_list)

# Filtra as músicas do artista que começa com a letra P
artists_starting_with_p = df[df["Artist"].str.startswith("P")]

# Agrupo o dataframe por artista e soma as semanas de cada artista
points_by_artist = artists_starting_with_p.groupby(
    'Artist', as_index=False
    ).agg({
      'Weeks in Charts': 'sum', 'Rank': 'first'
    })

# Ordena os artistas por pontuação e pega os 10 primeiros
top_10_artists = points_by_artist.nlargest(10, "Weeks in Charts")

# Reordena as colunas do Dataframe
top_10_artists = top_10_artists[['Rank', 'Artist', 'Weeks in Charts']]

# Renomea as colunas do Dataframe
top_10_artists.columns = ['Rank', 'Artist', 'Pontos']

# Remove o index do Dataframe
top_10_artists.reset_index(drop=True, inplace=True)

# Salva o Dataframe em um arquivo CSV
top_10_artists.to_csv("top_10_artists.csv", index=False)
