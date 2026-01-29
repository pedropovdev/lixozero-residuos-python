import pandas as pd
import folium

df = pd.read_csv("dados_residuos.csv")
# Mapa: Localização fictícia dos bairros
residuos_bairro = df.groupby("bairro")["toneladas"].sum().reset_index()

# Coordenadas fictícias para os bairros
coordenadas = {
    "centro": [-23.55052, -46.633308],
    "zona norte": [-23.500000, -46.600000],
    "zona sul": [-23.600000, -46.650000],
    "zona leste": [-23.550000, -46.580000],
    "zona oeste": [-23.560000, -46.700000],
}

#criar mapa
mapa = folium.Map(location = [-23.55052, -46.633308], zoom_start=12)

#adicionar pontos
for _, row in residuos_bairro.iterrows():
    bairro = row["bairro"]
    total = round(row["toneladas"], 2)
    lat, lon = coordenadas[bairro]

    folium.Marker(
        location=[lat, lon],
        popup=f"{bairro}<br>Total anual: {total} toneladas",
        icon = folium.Icon(color="green", icon="trash ")).add_to(mapa)
#salvar mapa
mapa.save("reports/mapa_residuos.html")
print("Mapa 'mapa_residuos.html' gerado com sucesso.")