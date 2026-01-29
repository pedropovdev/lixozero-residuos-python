import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_residuos.csv")

# Análise: Total de toneladas coletadas por tipo de resíduo
total_por_bairro = df.groupby("bairro") ["toneladas"].sum()

#grafico
plt.figure()
total_por_bairro.plot(kind = "bar")
plt.title("Total de resíduos coletados por bairro(Toneladas/ano)")
plt.ylabel("Toneladas")
plt.xlabel("Bairro")
plt.tight_layout()
plt.show()
