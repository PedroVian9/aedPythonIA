import pandas as pd
from grafico_distribuicao import plot_distribuicao_final_semana
from grafico_precipitacao import plot_precipitacao_temporal

def carregar_dados(beer_consuption: str):
    return pd.read_csv(beer_consuption, sep=',') 

def exibir_dimensoes(df: pd.DataFrame):
    print(f"\n({df.shape[0]}, {df.shape[1]})")

def verificar_tipos_dados(df: pd.DataFrame):
    print("\nTipos de dados por coluna:")
    print(df.dtypes)

def verificar_valores_faltantes(df: pd.DataFrame):
    print("\nValores faltantes por coluna:")
    print(df.isna().sum())

def exibir_primeiras_linhas(df: pd.DataFrame, n: int = 5):
    print("\nPrimeiras linhas:")
    print(df.head(n))

def exibir_ultimas_linhas(df: pd.DataFrame, n: int = 5):
    print("\nÚltimas linhas:")
    print(df.tail(n))

def executar_todas_analises(df: pd.DataFrame):
    """Executa todas as análises automaticamente"""
    print("\n" + "="*50)
    print(" EXECUTANDO TODAS AS ANÁLISES AUTOMATICAMENTE ")
    print("="*50)
    
    # Dimensões
    print("\n[1] DIMENSÕES DO DATASET")
    exibir_dimensoes(df)
    
    # Tipos de dados
    print("\n[2] TIPOS DE DADOS")
    verificar_tipos_dados(df)
    
    # Valores faltantes
    print("\n[3] VALORES FALTANTES")
    verificar_valores_faltantes(df)
    
    # Estatísticas
    print("\n[4] RESUMO ESTATÍSTICO")
    print(df.describe())
    
    # Primeiras linhas
    print("\n[5] PRIMEIRAS LINHAS")
    exibir_primeiras_linhas(df)
    
    # Últimas linhas
    print("\n[6] ÚLTIMAS LINHAS")
    exibir_ultimas_linhas(df)
    
    print("\n" + "="*50)
    print(" ANÁLISES COMPLETAS ")
    print("="*50)

def menu_interativo():
    print("\n=== ANÁLISE DE DADOS DE CERVEJA ===")
    arquivo = 'beer_consuption.csv'
    
    try:
        df = carregar_dados(arquivo)
        print(f"\n✅ Arquivo '{arquivo}' carregado com sucesso!")
        
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. Exibir primeiras linhas")
            print("2. Exibir últimas linhas")
            print("3. Visualizar resumo estatístico")
            print("4. Mostrar dimensões do dataset")
            print("5. Verificar valores faltantes")
            print("6. Verificar tipos de dados")
            print("7. Gráfico: Distribuição de finais de semana")  
            print("8. Gráfico: Precipitação ao longo do tempo")    
            print("99. Executar TODAS as análises")
            print("0. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                n = int(input("Quantas linhas deseja ver? (Padrão: 5) ") or 5)
                exibir_primeiras_linhas(df, n)
            elif opcao == "2":
                n = int(input("Quantas linhas deseja ver? (Padrão: 5) ") or 5)
                exibir_ultimas_linhas(df, n)
            elif opcao == "3":
                print("\nResumo estatístico:")
                print(df.describe())
            elif opcao == "4":
                exibir_dimensoes(df)
            elif opcao == "5":
                verificar_valores_faltantes(df)
            elif opcao == "6":
                verificar_tipos_dados(df)
            elif opcao == "7":
                plot_distribuicao_final_semana(df)
            elif opcao == "8":
                plot_precipitacao_temporal(df)
            elif opcao == "99":
                executar_todas_analises(df)
            elif opcao == "0":
                print("\nSaindo do programa...")
                break
            else:
                print("\n⚠️ Opção inválida! Tente novamente.")
                
    except FileNotFoundError:
        print(f"\n❌ Erro: Arquivo '{arquivo}' não encontrado!")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    menu_interativo()