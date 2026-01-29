import pandas as pd
import numpy as np

np.random.seed(42)

bairros = ["centro", "zona norte", "zona sul", "zona leste", "zona oeste"]
tipos_residuos = ["orgânico", "reciclável", "perigoso", "eletrônico"]

dados = []

for bairro in bairros:
    for tipo in tipos_residuos:
        for mes in tipos_residuos:
            quantidade = np.random.uniform(100, 1000)
            dados.append([
                bairro,
                tipo,
                mes,
                round(quantidade, 2)
            ])
df = pd.DataFrame(
    dados,
    columns=["bairro", "tipo_residuo", "mes", "toneladas"])

df.to_csv("dados_residuos.csv", index=False)

print("Arquivo 'dados_residuos.csv' gerado com sucesso.")
# Gerar dados fictícios sobre coleta de resíduos sólidos urbanos

