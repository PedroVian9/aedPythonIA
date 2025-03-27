import pandas as pd
from grafico_finalDeSemana import plot_distribuicao_final_semana
from grafico_precipitacao import plot_precipitacao_temporal
from grafico_precipitacaoDiaria import plot_temperaturas
from grafico_consumoCerveja import plot_consumo_cerveja

# Carregando Arquivo
def carregar_dados(beer_consuption: str):
    return pd.read_csv(beer_consuption, sep=',') 

# (c) Primeiras observações do arquivo do beer_consumption.csv;
def exibir_primeiras_linhas(df: pd.DataFrame, n: int = 5):
    print(df.head(n))

# (d) Últimas observações do arquivo do beer_consumption.csv;
def exibir_ultimas_linhas(df: pd.DataFrame, n: int = 5):
    print(df.tail(n))

# (e) Ver a dimensão da base de dados: são 365 observações e 7 variáveis;
def exibir_dimensoes(df: pd.DataFrame):
    print(f"\n({df.shape[0]}, {df.shape[1]})")

# (f) Verificar se existe valores faltantes na base de dados
def verificar_valores_faltantes(df: pd.DataFrame):
    print(df.isna().sum())

# (g) Verificar o tipo das variáveis
def verificar_tipos_dados(df: pd.DataFrame):
    print(df.dtypes)

# (h) Correlação entre as variáveis
def exibir_correlacao(df: pd.DataFrame):
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    correlacao = numeric_df.corr()
    print(correlacao.to_string(float_format="%.6f"));

# (i) Tabela descritiva das variáveis (discribe)
def exibir_tabela_descritiva(df: pd.DataFrame):
    print(df.describe().to_string())

# (j) Produza um gráfico para a variável Final de Semana
# (k) Gráfico das temperaturas média, mínima e máxima 
# (l)  Gráfico da precipitação diária
# (m) Gráfico do consumo de cerveja


def menu_interativo():
    print("\n=== ANÁLISE DE DADOS DE CERVEJA ===")
    arquivo = 'beer_consuption.csv'
    
    try:
        df = carregar_dados(arquivo)
        print(f"\n✅ Arquivo '{arquivo}' carregado com sucesso!")

        while True:
            print("\nMenu de Opções:")
            print("(c) Primeiras observações do arquivo do beer_consumption.csv")
            print("(d) Últimas observações do arquivo do beer_consumption.csv")
            print("(e) Ver a dimensão da base de dados: são 365 observações e 7 variáveis")
            print("(f) Verificar se existe valores faltantes na base de dados")
            print("(g) Verificar o tipo das variáveis")
            print("(h) Correlação entre as variáveis")
            print("(i) Tabela descritiva das variáveis (discribe)")
            print("(j) Produza um gráfico para a variável Final de Semana.")
            print("(k) Gráfico das temperaturas média, mínima e máxima")
            print("(l)  Gráfico da precipitação diária")
            print("(m) Gráfico do consumo de cerveja")
            print("(sair) Sair")
            
            opcao = input("\nDigite a letra da opção desejada: ").lower()
            
            if opcao == 'c':
                n = int(input("Quantas linhas deseja visualizar? (padrão: 5) ") or 5)
                exibir_primeiras_linhas(df, n)
            elif opcao == 'd':
                n = int(input("Quantas linhas deseja visualizar? (padrão: 5) ") or 5)
                exibir_ultimas_linhas(df, n)
            elif opcao == 'e':
                exibir_dimensoes(df)
            elif opcao == 'f':
                verificar_valores_faltantes(df)
            elif opcao == 'g':
                verificar_tipos_dados(df)
            elif opcao == 'h':
                exibir_correlacao(df)
            elif opcao == 'i':
                exibir_tabela_descritiva(df)
            elif opcao == 'j':
                plot_distribuicao_final_semana(df)
            elif opcao == 'k':
                plot_temperaturas(df)
            elif opcao == 'l':
                plot_precipitacao_temporal(df)
            elif opcao == 'm':
                plot_consumo_cerveja(df)    
            elif opcao == 'sair':
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida! Por favor, digite uma letra válida.")
            
            input("\nPressione Enter para continuar...")

    except FileNotFoundError:
        print(f"\n❌ Erro: Arquivo '{arquivo}' não encontrado!")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro: {str(e)}")


if __name__ == "__main__":
    menu_interativo()