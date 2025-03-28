import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

def plot_boxplots_outliers(df: pd.DataFrame):
    numeric_cols = ['Temperatura Media (C)', 'Temperatura Minima (C)', 
                   'Temperatura Maxima (C)', 'Precipitacao (mm)', 
                   'Consumo de cerveja (litros)']
    
    plt.figure(figsize=(10, 8))
    sns.boxplot(data=df[numeric_cols], orient="v", palette="Set2")
    plt.title('Análise de Outliers nas Variáveis Numéricas', pad=20)
    plt.ylabel('Valores')
    plt.xlabel('Variáveis')
    plt.xticks(rotation=45) 
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()
    
    print("\n🔍 Análise de Outliers:")
    for col in numeric_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        num_outliers = len(outliers)
        
        print(f"\n• {col}:")
        print(f"   - Limite inferior: {lower_bound:.2f}")
        print(f"   - Limite superior: {upper_bound:.2f}")
        print(f"   - Número de outliers: {num_outliers}")
        
        if num_outliers > 0:
            print(f"   - Valores outliers: {outliers[col].values.round(2)}")