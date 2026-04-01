"""
Carrega dados brutos do CSV
"""
import pandas as pd

def load_raw_data(filepath):
    """
    Carrega dados brutos do CSV
    
    Args:
        filepath (str): Caminho do arquivo CSV
        
    Returns:
        pd.DataFrame: DataFrame bruto
    """
    df = pd.read_csv(filepath, low_memory=False)
    print(f"✅ Carregados {len(df):,} imóveis com {len(df.columns)} colunas")
    return df
