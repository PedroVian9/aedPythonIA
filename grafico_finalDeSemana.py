import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribuicao_final_semana(df):
    try:
        plt.figure(figsize=(8, 5))
        df['Final de Semana'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
        plt.title('Distribuição de Final de Semana', pad=20)
        plt.xlabel('Final de Semana (0 = Não, 1 = Sim)')
        plt.ylabel('Frequência')
        plt.xticks(rotation=0)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        print("\n📊 Gráfico de distribuição de finais de semana exibido")
        plt.show()
    except KeyError:
        print("❌ Coluna 'Final de Semana' não encontrada no DataFrame")
    except Exception as e:
        print(f"❌ Erro ao gerar gráfico: {str(e)}")
