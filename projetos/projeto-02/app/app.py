import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Path ABSOLUTO (funciona sempre)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'tb_completo_com_metricas.csv')

df = pd.read_csv(DATA_PATH)

st.set_page_config(layout="wide")
st.title("🦠 TB Mundial")

pais = st.sidebar.selectbox("País:", ['World'] + sorted(df['Country Name'].unique().tolist()))
df_filt = df[df['Country Name'] == pais].sort_values('Year')

col1, col2 = st.columns(2)
col1.metric("Incidência Média", f"{df_filt['incidence_per_100k'].mean():.1f}")
col2.metric("Status Atual", df_filt['controle_status'].iloc[-1])

col1, col2 = st.columns(2)
fig1 = px.line(df_filt, x='Year', y='incidence_per_100k')
col1.plotly_chart(fig1, use_container_width=True)

fig2 = px.pie(df, names='controle_status')
col2.plotly_chart(fig2, use_container_width=True)

st.dataframe(df_filt)
