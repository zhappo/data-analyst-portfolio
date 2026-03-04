# 📊 Análise de Vendas — Superstore West (2014–2017)

> **Altas vendas nem sempre significam alto lucro.**  
> Este projeto investiga por que a categoria com maior volume de vendas na região Oeste fechou no vermelho — e o que os dados revelam sobre a política de descontos.

---

## 🔍 Problema de Negócio

Ao analisar o dataset Superstore (região West, 2014–2017), surgiu uma anomalia: **Furniture liderava em vendas, mas registava prejuízo líquido de -$2K**. Technology, com volume praticamente igual, gerava **$37K de lucro**.

A análise foi conduzida para responder: **por que altas vendas não se traduzem em alto lucro?**

---

## 💡 Principais Insights

| Categoria       | Vendas Totais | Lucro     | Ticket Médio |
|----------------|---------------|-----------|--------------|
| Furniture       | $253K (34,8%) | **-$2K**  | $100         |
| Technology      | $252K (34,7%) | **+$37K** | $421         |
| Office Supplies | $221K (30,4%) | **+$22K** | $116         |

- 📉 **Correlação Desconto × Lucro: -0.22** — quanto maior o desconto, menor o lucro
- ⚠️ Descontos acima de 20% resultaram em **lucro negativo em 60% dos casos**
- 🪑 A combinação **Furniture + desconto agressivo** foi a mais destrutiva para a margem da região

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat)
![Google Colab](https://img.shields.io/badge/Google_Colab-F9AB00?style=flat&logo=googlecolab&logoColor=white)

---

## 📁 Estrutura do Projeto

```
📦 superstore-west-analysis
 ┣ 📓 semana_1.ipynb       # Notebook principal com análise completa
 ┗ 📄 README.md
```

O dataset é carregado automaticamente via URL pública:
```
https://raw.githubusercontent.com/yajasarora/Superstore-Sales-Analysis-with-Tableau/master/Superstore%20sales%20dataset.csv
```
*(9.994 linhas · 21 colunas)*

---

## ▶️ Como Executar

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# 2. Instale as dependências
pip install pandas matplotlib seaborn

# 3. Abra o notebook
jupyter notebook semana_1.ipynb
```

Ou execute diretamente no **Google Colab** — sem instalação necessária.

---

## 📋 Etapas da Análise

1. **Limpeza de dados** — tratamento de duplicatas e padronização
2. **Filtro por região** — foco exclusivo na região Oeste (West)
3. **EDA por categoria** — vendas, lucro e ticket médio por categoria e subcategoria
4. **Análise temporal** — evolução de vendas por ano (2014–2017)
5. **Análise de correlação** — heatmap entre Vendas, Lucro e Desconto
6. **Conclusões e recomendações** — insights acionáveis para o negócio

---

## ✅ Recomendações Estratégicas

1. **Limitar descontos a 20%** — descontos acima desse patamar geram prejuízo comprovado
2. **Reavaliar o mix de Furniture** — identificar e descontinuar itens com margem cronicamente negativa
3. **Investir em Technology** — melhor relação volume-lucro da região
4. **Monitoramento contínuo** — dashboards com alertas automáticos de margem

---

## 👤 Autor

Feito por **[Osvaldo Oliveira]** · [LinkedIn](https://www.linkedin.com/in/osvaldo-oliveira-jr/) · [GitHub](https://github.com/zhappo)

> Estou em transição para a área de dados e aberto a oportunidades como Analista de Dados Jr. Vamos conversar! 🙂
