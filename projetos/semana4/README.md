# Hotel Bookings: Análise de Cancelamentos (EDA)

## 🎯 **Objetivo**

Com base no **hotel_booking.csv** analisar os dados refrentes aos cancelamentos** de em 119k reservas (2015-2017) de **City Hotel** vs **Resort Hotel** para insights de Revenue Management.

## 📊 **Principais Insights**

| Insight | Taxa Cancel | Ação Possível |
|---------|-------------|---------------|
| **Resort 27.8%** | vs City 24.8% | Política cancelamento mais rígida Resort |
| **Junho 49%** | pico cancel | Promoções early booking junho |
| **>90 dias 60%** | risco alto | Email follow-up reservas antigas |
| **Cancel ~50€** | vs 90€ confirmações | Testar preço mínimo para reduzir voláteis |


## 🛠️ **Tech Stack**

- **Python 3.11** | pandas | matplotlib | seaborn
- **IDE**: VSCode + Jupyter | **OS**: Linux Mint Debian
- **Tempo**: 90min análise completa


## 📈 **Visualizações Geradas**

- `avg_cancel_hotel.png`: Bar Resort vs City 
- `cancelmes.png`:  Line sazonalidade meses (Junho pico)
- `leadtimecancel.png`: Scatter lead time x cancelamento
- `adrcancelboxplot.png`: Boxplot ADR cancelado vs confirmado

***

**Osvaldo Oliveira Jr** | Data Analyst | **25/Mar/2026** | [exploracao.ipynb](exploracao.ipynb)

<div align="center">⁂</div>

[^1]: exploracao.ipynb

