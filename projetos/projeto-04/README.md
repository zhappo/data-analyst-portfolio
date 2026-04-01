# 🏠 Análise Imobiliária em Portugal

Dashboard interativo explorando padrões de preços de imóveis em Portugal com base em 135k+ listagens. Identifica oportunidades de investimento por região, tipo de imóvel e certificado energético.

## 📊 Objetivo

Desenvolver uma análise exploratória completa e um dashboard interativo que permita:
- Explorar distribuição de preços por distrito
- Comparar tipos de imóveis (apartamentos vs casas)
- Analisar influência do certificado energético no valor
- Identificar tendências de preço/m² por região
- Filtrar dados interativamente em tempo real

## ❓ Perguntas Respondidas

- ✅ Qual é a distribuição de preços por distrito português?
- ✅ Como o certificado energético influencia o valor do imóvel?
- ✅ Qual é o preço/m² em Lisboa vs outras regiões?
- ✅ Que tipo de imóvel (apartamento vs casa) oferece melhor custo-benefício?
- ✅ Existe relação entre área e preço?

## 📈 Dataset

| Atributo | Valor |
|----------|-------|
| **Fonte** | Kaggle - Real Estate Listings in Portugal 2024 |
| **Linhas** | 135.236 imóveis |
| **Colunas** | 25 atributos |
| **Cobertura** | Todos os distritos de Portugal |
| **Período** | Dataset estável 2024 |

## 🎯 Principais Insights

- **Apartamentos**: 11.2% mais caros que casas (€298.500 vs €265.000)
- **Braga**: 30.7% mais barata que a média nacional (€1.667/m² vs €2.404/m²)
- **Certificado A+**: 50.9% de premium
- **Correlação Forte**: Existe relação positiva entre área e preço

## 🛠️ Ferramentas & Tecnologias

| Ferramenta | Uso |
|-----------|-----|
| **Python 3.11+** | Linguagem principal |
| **Pandas** | Manipulação e limpeza de dados |
| **NumPy** | Operações numéricas |
| **Plotly** | Visualizações interativas |
| **Streamlit** | Dashboard web |
| **Jupyter** | Análise exploratória |

## 📁 Estrutura do Projeto

```
semana_05/
├── requirements.txt
├── README.md
├── app.py
├── notebooks/
│   └── exploracao.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_cleaner.py
│   └── data_processor.py
└── data/
    └── raw/
        └── portugal_listinigs.csv
```
