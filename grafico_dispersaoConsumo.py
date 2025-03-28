import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_dispersao_consumo(df: pd.DataFrame):
    plt.figure(figsize=(15, 10))
    
    variaveis = ['Temperatura Media (C)', 'Temperatura Minima (C)', 
                'Temperatura Maxima (C)', 'Precipitacao (mm)']
    
    for i, var in enumerate(variaveis, 1):
        plt.subplot(2, 2, i)
        
        sns.scatterplot(data=df, x='Consumo de cerveja (litros)', y=var,
                       color='#1f77b4', alpha=0.7, s=60)
        
        plt.xlabel('Consumo de cerveja (litros)')
        plt.ylabel(var)
        plt.grid(alpha=0.2)
        

    plt.tight_layout(pad=2.5)
    plt.show()