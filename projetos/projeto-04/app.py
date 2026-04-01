import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.data_loader import load_raw_data
from src.data_cleaner import clean_data
from src.data_processor import process_data, get_district_stats, get_type_stats, get_energy_stats

# Config página
st.set_page_config(page_title="Análise Imobiliária PT", layout="wide", initial_sidebar_state="expanded")

# Título
st.title("🏠 Análise Imobiliária em Portugal - Semana 5")
st.markdown("Dashboard interativo com dados imobiliários portugueses. Explore preços, regiões e oportunidades de investimento.")

# Cache para carregar dados uma só vez
@st.cache_data
def load_and_process_data():
    df_raw = load_raw_data("data/raw/portugal_listinigs.csv")
    df_clean = clean_data(df_raw)
    df_final, stats = process_data(df_clean)
    return df_final, stats

# Carrega dados
df_final, stats = load_and_process_data()

# Sidebar - Filtros e controle
st.sidebar.header("🔍 Filtros")

# Botões de controle    
col1, col2 = st.sidebar.columns(2)
with col1:
    select_all = st.button("✅ Todos", key="select_all_btn")
with col2:
    clear_all = st.button("🔄 Limpar", key="clear_all_btn")

# Districts
all_districts = sorted(df_final['District'].unique())
if select_all:
    st.session_state.selected_districts = all_districts
elif clear_all:
    st.session_state.selected_districts = []

selected_districts = st.sidebar.multiselect(
    "Selecione Distritos",
    options=all_districts,
    default=st.session_state.get('selected_districts', ['Vila Real', 'Braga', 'Viana do Castelo', 'Porto','Lisboa']),
    key="districts_filter"
)

# Se vazio após limpeza, força padrão
if not selected_districts:
    selected_districts = all_districts[:5]

# Types
all_types = sorted(df_final['Type'].unique())
default_types = [t for t in all_types if t in ['Apartment', 'House']]
if not default_types:
    default_types = all_types[:2]

selected_types = st.sidebar.multiselect(
    "Selecione Tipos de Imóvel",
    options=all_types,
    default=default_types,
    key="types_filter"
)

if not selected_types:
    selected_types = default_types

# Filtra dados
df_filtered = df_final[
    (df_final['District'].isin(selected_districts)) & 
    (df_final['Type'].isin(selected_types))
]

st.sidebar.divider()
st.sidebar.caption(f"📊 {len(df_filtered):,} imóveis filtrados")

# KPIs
st.subheader("📊 KPIs Principais")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Imóveis", f"{len(df_filtered):,}")
with col2:
    st.metric("Preço Mediano", f"€{df_filtered['Price'].median():,.0f}")
with col3:
    st.metric("Preço/m² Mediano", f"€{df_filtered['PricePerM2'].median():,.0f}")
with col4:
    st.metric("Distritos", df_filtered['District'].nunique())

st.divider()

# Row 1: Distribuição Preços + Top Distritos
col1, col2 = st.columns(2)

with col1:
    fig_price = px.histogram(
        df_filtered,
        x='Price',
        nbins=50,
        title='📈 Distribuição de Preços',
        labels={'Price': 'Preço (€)'},
        color_discrete_sequence=['#1f77b4']
    )
    fig_price.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig_price, use_container_width=True)

with col2:
    district_stats = df_filtered.groupby('District')['Price'].median().sort_values(ascending=True).head(10)
    fig_district = px.bar(
        x=district_stats.values,
        y=district_stats.index,
        orientation='h',
        title='🏘️ Top 10 Distritos - Preço Mediano',
        labels={'x': 'Preço Mediano (€)', 'y': 'Distrito'},
        color=district_stats.values,
        color_continuous_scale='Viridis'
    )
    fig_district.update_layout(height=400)
    st.plotly_chart(fig_district, use_container_width=True)

st.divider()

# Row 2: Tipo + Energy Certificate
col1, col2 = st.columns(2)

with col1:
    fig_type = px.box(
        df_filtered,
        x='Type',
        y='Price',
        title='🏠 Preço por Tipo de Imóvel',
        labels={'Price': 'Preço (€)', 'Type': 'Tipo'},
        color='Type'
    )
    fig_type.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig_type, use_container_width=True)

with col2:
    energy_data = df_filtered[df_filtered['EnergyCertificate'].notna()]
    if len(energy_data) > 0:
        fig_energy = px.box(
            energy_data,
            x='EnergyCertificate',
            y='Price',
            title='⚡ Preço por Certificado Energético',
            labels={'Price': 'Preço (€)', 'EnergyCertificate': 'Certificado'},
            color='EnergyCertificate'
        )
        fig_energy.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_energy, use_container_width=True)

st.divider()

# Row 3: Preço/m² + Scatter
col1, col2 = st.columns(2)

with col1:
    priceperm2_stats = df_filtered.groupby('District')['PricePerM2'].median().sort_values(ascending=True).head(10)
    fig_priceperm2 = px.bar(
        x=priceperm2_stats.values,
        y=priceperm2_stats.index,
        orientation='h',
        title='💰 Top 10 - Preço/m² por Distrito',
        labels={'x': 'Preço/m² (€)', 'y': 'Distrito'},
        color=priceperm2_stats.values,
        color_continuous_scale='RdYlGn_r'
    )
    fig_priceperm2.update_layout(height=400)
    st.plotly_chart(fig_priceperm2, use_container_width=True)

with col2:
    numeric_data = df_filtered[['Price', 'TotalArea', 'NumberOfBedrooms']].dropna()
    if len(numeric_data) > 100:
        fig_scatter = px.scatter(
            df_filtered.dropna(subset=['TotalArea', 'Price']).sample(min(1000, len(df_filtered))),
            x='TotalArea',
            y='Price',
            title='📊 Relação: Área vs Preço',
            labels={'TotalArea': 'Área (m²)', 'Price': 'Preço (€)'},
            color='PricePerM2',
            color_continuous_scale='Viridis',
            opacity=0.6
        )
        fig_scatter.update_layout(height=400)
        st.plotly_chart(fig_scatter, use_container_width=True)

st.divider()

# Insights
st.subheader("💡 Insights Principais")
col1, col2, col3 = st.columns(3)

with col1:
    st.info(f"**Apartamentos**: {stats['apt_premium']}% mais caros que casas")
with col2:
    if stats['braga_diff'] is not None:
        st.info(f"**Braga**: {stats['braga_diff']}% vs média Portugal")
    else:
        st.info("**Braga**: Sem dados")
with col3:
    if stats['energy_a_plus'] is not None:
        st.info(f"**Certificado A+**: {stats['energy_a_plus']}% premium")
    else:
        st.info("**Certificado A+**: Sem dados")

st.divider()

# Tabela de dados
st.subheader("📋 Dados Filtrados")
display_cols = ['Price', 'District', 'Type', 'TotalArea', 'PricePerM2', 'NumberOfBedrooms', 'EnergyCertificate']
st.dataframe(
    df_filtered[display_cols].head(100),
    use_container_width=True,
    height=400
)

st.divider()

# Footer
st.markdown("""
---
**Fonte:** Kaggle - Real Estate Listings in Portugal 2024  
**Ferramentas:** Python, Pandas, Plotly, Streamlit  
**GitHub:** [github.com/zhappo](https://github.com/zhappo)  
**LinkedIn:** [osvaldo-oliveira-jr](https://www.linkedin.com/in/osvaldo-oliveira-jr/)
""")