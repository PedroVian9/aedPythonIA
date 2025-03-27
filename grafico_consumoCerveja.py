import matplotlib.pyplot as plt
import seaborn as sns

def plot_consumo_cerveja(df):
    try:
        plt.figure(figsize=(12, 6))
    
        plt.plot(df['Consumo de cerveja (litros)'], 
                color='black', 
                linewidth=2,
                label='Consumo diário')
        
        media = df['Consumo de cerveja (litros)'].mean()
        

        plt.title('Variação do Consumo de Cerveja (litros)', pad=20)
        plt.xlabel('Dias')
        plt.ylabel('Litros de cerveja')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend()
        
        y_min = df['Consumo de cerveja (litros)'].min() - 2
        y_max = df['Consumo de cerveja (litros)'].max() + 2
        plt.ylim(y_min if y_min > 0 else 0, y_max)
        
        plt.tight_layout()
        print("\n📊 Gráfico de consumo de cerveja exibido")
        plt.show()
        
    except KeyError:
        print("❌ Coluna 'Consumo de cerveja (litros)' não encontrada no DataFrame")
    except Exception as e:
        print(f"❌ Erro ao gerar gráfico de consumo: {str(e)}")