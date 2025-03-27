import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_temperaturas(df: pd.DataFrame):
    plt.figure(figsize=(12, 6))
    
    plt.plot(df['Temperatura Media (C)'], label='Média', color='blue', linewidth=2)
    plt.plot(df['Temperatura Minima (C)'], label='Mínima', color='green', linestyle='--')
    plt.plot(df['Temperatura Maxima (C)'], label='Máxima', color='red', linestyle='-.')
    
    plt.title('Variação das Temperaturas ao Longo do Tempo', fontsize=14)
    plt.xlabel('Dias', fontsize=12)
    plt.ylabel('Temperatura (°C)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    y_min = df['Temperatura Minima (C)'].min() - 2
    y_max = df['Temperatura Maxima (C)'].max() + 2
    plt.ylim(y_min, y_max)
    
    plt.tight_layout()
    plt.show()