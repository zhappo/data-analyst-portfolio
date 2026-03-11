# Dashboard de Tuberculose Mundial

Este projeto é um dashboard interativo em Python para explorar a evolução da tuberculose (TB) ao longo do tempo por país, utilizando dados em formato CSV e a biblioteca Streamlit para a interface web.

## Objetivo

Permitir que o utilizador:

- Visualize a tendência temporal da incidência de TB por país.
- Compare a situação de controle da TB entre países.
- Explore os dados filtrando por país e ano.

## Stack utilizada

- Python
- Streamlit
- Pandas
- Plotly

## Estrutura do projeto

```text
.
├── app/
│   └── app.py
├── data/
│   ├── raw/
│   │   └── API_SH.TBS.INCD_DS2_en_csv_v2_1949.csv  # Dados TB do Banco Mundial
│   └── processed/
│       └── tb_completo_com_metricas.csv
├── exploracao.ipynb
└── requirements.txt

