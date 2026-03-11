import pandas as pd

@st.cache_data
def load_tb_data():
    """Carrega dados processados TB"""
    return pd.read_csv('../../data/processed/tb_completo_com_metricas.csv')

def get_top_paises(df, top_n=10):
    """Top países por incidência média"""
    return (df.groupby('Country Name')['incidence_per_100k']
            .mean().sort_values(ascending=False).head(top_n))
