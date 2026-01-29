# ♻️ LixoZero — Análise e Monitoramento de Resíduos Sólidos Urbanos

## 📌 Contexto
A gestão de resíduos sólidos urbanos é um dos principais desafios ambientais no Brasil,
impactando diretamente a saúde pública, o meio ambiente e o planejamento urbano.

Apesar da grande quantidade de dados disponíveis, muitas vezes essas informações não são
transformadas em análises claras que auxiliem a tomada de decisão.

Este projeto nasce exatamente nesse ponto.

---

## 🎯 Objetivo
Desenvolver uma ferramenta em **Python** capaz de:
- organizar dados de resíduos sólidos urbanos,
- gerar indicadores ambientais relevantes,
- visualizar informações em mapas e gráficos,
- produzir relatórios automáticos em PDF.

O projeto utiliza **dados simulados**, com foco em aprendizado, estruturação e escalabilidade
para futura integração com dados reais.

---

## 🛠️ Tecnologias Utilizadas
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Folium  
- FPDF  

---

## 📊 Funcionalidades
✔️ Geração de dados simulados de resíduos sólidos  
✔️ Análise por bairro e tipo de resíduo  
✔️ Cálculo de indicadores ambientais básicos  
✔️ Visualização gráfica dos dados  
✔️ Mapa interativo com distribuição espacial dos resíduos  
✔️ Geração automática de relatório ambiental em PDF  

---

## 🗺️ Visualizações
- **Mapa interativo** com total anual de resíduos por bairro  
- **Gráficos** de distribuição e comparação  
- **Relatório PDF** consolidado com indicadores ambientais  

*(Imagens demonstrativas disponíveis na pasta `/imagens`)*

---

## 📁 Estrutura do Projeto
```bash
lixozero-residuos-solidos/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── gerar_dados.py
│   ├── analise.py
│   ├── mapa.py
│   └── relatorio.py
│
├── reports/
│   ├── mapa_residuos.html
│   └── relatorio_residuos.pdf
│
├── imagens/
├── main.py
├── requirements.txt
└── README.md
