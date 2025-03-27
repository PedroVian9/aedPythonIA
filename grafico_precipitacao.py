import matplotlib.pyplot as plt
import seaborn as sns

def plot_precipitacao_temporal(df):
    try:
        plt.figure(figsize=(12, 6))
        plt.plot(df['Precipitacao (mm)'], color='royalblue', label='Precipitação')
        plt.title('Precipitação ao Longo do Tempo', pad=20)
        plt.xlabel('Dias')
        plt.ylabel('Precipitação (mm)')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        print("\n📊 Gráfico de precipitação temporal exibido")
        plt.show()
    except KeyError:
        print("❌ Coluna 'Precipitacao (mm)' não encontrada no DataFrame")
    except Exception as e:
        print(f"❌ Erro ao gerar gráfico: {str(e)}")