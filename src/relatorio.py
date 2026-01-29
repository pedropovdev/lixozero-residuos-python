import pandas as pd
from fpdf import FPDF

# Ler dados
df = pd.read_csv("data/residuos_simulados.csv")

# Indicadores
total_geral = df["toneladas"].sum()
por_tipo = df.groupby("tipo_residuo")["toneladas"].sum()

# Criar PDF
pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Relatório Ambiental - Resíduos Sólidos", ln=True)

pdf.ln(5)
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, f"Total anual de resíduos: {total_geral:.2f} toneladas", ln=True)

pdf.ln(5)
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Distribuição por tipo:", ln=True)

pdf.set_font("Arial", size=12)
for tipo, valor in por_tipo.items():
    pdf.cell(0, 8, f"- {tipo}: {valor:.2f} toneladas", ln=True)

# Salvar PDF
pdf.output("reports/relatorio_residuos.pdf")

print("Relatório PDF gerado com sucesso!")
