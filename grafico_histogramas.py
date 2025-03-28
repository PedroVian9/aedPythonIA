import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_histogramas(df: pd.DataFrame):
    plt.figure(figsize=(12, 8)) 
    
    variaveis = ['Temperatura Media (C)', 'Temperatura Minima (C)', 
                'Temperatura Maxima (C)', 'Precipitacao (mm)', 
                'Consumo de cerveja (litros)']
    
    for i, var in enumerate(variaveis, 1):
        plt.subplot((len(variaveis)+1)//2, 2, i)
        
        sns.histplot(data=df, x=var, kde=True, color='dodgerblue', bins=12, alpha=0.7)
        plt.title(var, fontsize=11, pad=8)
        plt.grid(axis='y', alpha=0.2)
        
        if i == 1: 
            plt.legend(['Média', 'Mediana'], fontsize=8)

    plt.tight_layout(pad=1.5)
    plt.show()