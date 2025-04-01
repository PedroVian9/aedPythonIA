import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def plot_correlacao_pearson(df: pd.DataFrame):
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    corr = numeric_df.corr()
    
    plt.figure(figsize=(10, 8))
    
    sns.heatmap(corr, 
                annot=True, 
                fmt=".2f", 
                cmap='coolwarm', 
                center=0,
                linewidths=0.5, 
                linecolor='black',
                cbar_kws={"shrink": 0.8})
    
    plt.title('Correlação de Pearson entre Variáveis', pad=20, fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    
    plt.show()