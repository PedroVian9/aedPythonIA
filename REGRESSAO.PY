import numpy as np
import pandas as pd

def carregar_dados(arquivo):
    return pd.read_csv(arquivo, sep=',')

def minimos_quadrados(x, y):
    x_mean, y_mean = np.mean(x), np.mean(y)
    b1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
    return y_mean - b1 * x_mean, b1

def gradiente_descendente(x, y, lr=0.0001, epochs=10000):
    m, b, n = 0.0, 0.0, len(x)
    x_norm, y_norm = (x - np.mean(x))/np.std(x), (y - np.mean(y))/np.std(y)
    
    for _ in range(epochs):
        erro = (m * x_norm + b) - y_norm
        m -= lr * (2/n) * np.sum(erro * x_norm)
        b -= lr * (2/n) * np.sum(erro)
    
    m_final = m * (np.std(y)/np.std(x))
    return np.mean(y) - m_final * np.mean(x), m_final

def calcular_metricas(x, y, b0, b1):
    y_pred = b1 * x + b0
    ss_res, ss_tot = np.sum((y - y_pred)**2), np.sum((y - np.mean(y))**2)
    r2 = 1 - (ss_res/ss_tot) if ss_tot != 0 else 0
    mse = np.mean((y - y_pred)**2)
    with np.errstate(divide='ignore', invalid='ignore'):
        mape = np.mean(np.abs(np.where(y != 0, (y - y_pred)/y, 0))) * 100
    return r2, mse, np.sqrt(mse), np.mean(np.abs(y - y_pred)), mape

def formatar_saida(b0_mmq, b1_mmq, b0_gd, b1_gd, metrica_mmq, metrica_gd):
    return (
        f"Coeficientes da Regressão Linear\n"
        f"MMQ - Intercepto: {b0_mmq:.6f} | Inclinação: {b1_mmq:.6f}\n"
        f"GD - Intercepto: {b0_gd:.6f} | Inclinação: {b1_gd:.6f}\n\n"
        f"Métricas MMQ:\n"
        f"R²: {metrica_mmq[0]:.6f} | MSE: {metrica_mmq[1]:.6f}\n"
        f"RMSE: {metrica_mmq[2]:.6f} | MAE: {metrica_mmq[3]:.6f}\n"
        f"MAPE: {metrica_mmq[4]:.2f}%\n\n"
        f"Métricas GD:\n"
        f"R²: {metrica_gd[0]:.6f} | MSE: {metrica_gd[1]:.6f}\n"
        f"RMSE: {metrica_gd[2]:.6f} | MAE: {metrica_gd[3]:.6f}\n"
        f"MAPE: {metrica_gd[4]:.2f}%"
    )

def executar_analise(arquivo):
    try:
        df = carregar_dados(arquivo)
        x = df['Temperatura Media (C)'].values.astype(float)
        y = df['Consumo de cerveja (litros)'].values.astype(float)
        
        if len(x) != len(y):
            print("Erro: Dados inconsistentes")
            return

        b0_mmq, b1_mmq = minimos_quadrados(x, y)
        b0_gd, b1_gd = gradiente_descendente(x, y)
        
        print(formatar_saida(
            b0_mmq, b1_mmq, b0_gd, b1_gd,
            calcular_metricas(x, y, b0_mmq, b1_mmq),
            calcular_metricas(x, y, b0_gd, b1_gd)
        ))
        
    except Exception as e:
        print(f"Erro: {str(e)}")

def menu_interativo():
    while True:
        print("\nREGRESSÃO LINEAR")
        opcao = input("1-Analisar / 2-Sair: ").strip()
        if opcao == '1': executar_analise('beer_consuption.csv')
        elif opcao == '2': return print("Saindo...")
        else: print("Opção inválida")

if __name__ == "__main__":
    menu_interativo()