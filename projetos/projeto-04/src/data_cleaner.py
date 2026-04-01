"""
Limpa e valida dados brutos
"""
import pandas as pd

def clean_data(df_raw):
    """
    Limpa dados brutos de imóveis
    
    Operações:
    - Remove preços < 10k€ e > 5M€
    - Remove áreas negativas ou > 100k m²
    - Remove dormitórios > 10
    - Remove linhas sem Price e TotalArea
    
    Args:
        df_raw (pd.DataFrame): DataFrame bruto
        
    Returns:
        pd.DataFrame: DataFrame limpo
    """
    df_clean = df_raw.copy()
    
    initial_count = len(df_clean)
    
    # Filtro 1: Preços válidos
    df_clean = df_clean[(df_clean['Price'] >= 10000) & (df_clean['Price'] <= 5000000)]
    
    # Filtro 2: Áreas válidas
    df_clean = df_clean[(df_clean['TotalArea'] > 0) & (df_clean['TotalArea'] <= 100000)]
    
    # Filtro 3: Dormitórios válidos
    df_clean = df_clean[(df_clean['NumberOfBedrooms'] >= 0) & (df_clean['NumberOfBedrooms'] <= 10)]
    
    # Filtro 4: Remove nulos essenciais
    df_clean = df_clean.dropna(subset=['Price', 'TotalArea', 'District', 'Type'])
    
    removed = initial_count - len(df_clean)
    removal_pct = (removed / initial_count) * 100
    
    print(f"🧹 Limpeza concluída:")
    print(f"   Antes: {initial_count:,} imóveis")
    print(f"   Depois: {len(df_clean):,} imóveis")
    print(f"   Removidos: {removed:,} ({removal_pct:.1f}%)")
    
    return df_clean
