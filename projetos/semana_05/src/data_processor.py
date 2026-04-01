"""
Processa dados limpos para análises e visualizações
"""
import pandas as pd

def process_data(df_clean):
    """
    Processa dados limpos
    
    Operações:
    - Cria coluna PricePerM2
    - Calcula estatísticas principais
    
    Args:
        df_clean (pd.DataFrame): DataFrame limpo
        
    Returns:
        tuple: (df_processado, dict_estatísticas)
    """
    df = df_clean.copy()
    
    # Coluna útil
    df['PricePerM2'] = df['Price'] / df['TotalArea']
    
    # Calcula estatísticas
    stats = {
        'apt_premium': calculate_apt_premium(df),
        'braga_diff': calculate_braga_diff(df),
        'energy_a_plus': calculate_energy_premium(df),
        'total_imoveis': len(df),
        'preco_mediano': df['Price'].median(),
        'preco_medio': df['Price'].mean(),
        'priceperм2_mediano': df['PricePerM2'].median()
    }
    
    print(f"📊 Processamento concluído:")
    print(f"   Total: {stats['total_imoveis']:,} imóveis")
    print(f"   Preço mediano: €{stats['preco_mediano']:,.0f}")
    print(f"   Preço/m² mediano: €{stats['priceperм2_mediano']:,.0f}")
    
    return df, stats

def calculate_apt_premium(df):
    """Calcula premium apartamento vs casa"""
    apt = df[df['Type'] == 'Apartment']['Price'].median()
    house = df[df['Type'] == 'House']['Price'].median()
    premium = ((apt - house) / house) * 100
    return round(premium, 1)

def calculate_braga_diff(df):
    """Calcula diferença Braga vs Portugal"""
    if 'Braga' not in df['District'].values:
        return None
    braga = df[df['District'] == 'Braga']['PricePerM2'].median()
    portugal = df['PricePerM2'].median()
    diff = ((braga - portugal) / portugal) * 100
    return round(diff, 1)

def calculate_energy_premium(df):
    """Calcula premium certificado A+"""
    energy_df = df[df['EnergyCertificate'].notna()]
    if 'A+' not in energy_df['EnergyCertificate'].values:
        return None
    a_plus = energy_df[energy_df['EnergyCertificate'] == 'A+']['Price'].median()
    geral = df['Price'].median()
    premium = ((a_plus - geral) / geral) * 100
    return round(premium, 1)

def get_district_stats(df, top_n=10):
    """Top N distritos por preço mediano"""
    return df.groupby('District')['Price'].agg(['median', 'mean', 'count']).sort_values('median', ascending=False).head(top_n)

def get_type_stats(df):
    """Estatísticas por tipo de imóvel"""
    return df.groupby('Type')['Price'].agg(['median', 'mean', 'count']).sort_values('median', ascending=False)

def get_energy_stats(df):
    """Estatísticas por certificado energético"""
    energy_df = df[df['EnergyCertificate'].notna()]
    return energy_df.groupby('EnergyCertificate')['Price'].agg(['median', 'mean', 'count']).sort_values('median', ascending=False)
