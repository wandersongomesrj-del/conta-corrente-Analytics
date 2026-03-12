import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar e limpar nomes de colunas
df = pd.read_csv('Chapter2-AccountData.csv')
df.columns = df.columns.str.strip()

# 2. Converter valores financeiros para números
df['Transaction Amount'] = df['Transaction Amount'].replace(r'[\$,]', '', regex=True).astype(float)
df['Balance'] = df['Balance'].replace(r'[\$,]', '', regex=True).astype(float)

# 3. Cálculos de resumo
total_gasto = df[df['Transaction Amount'] < 0]['Transaction Amount'].sum()
total_recebido = df[df['Transaction Amount'] > 0]['Transaction Amount'].sum()
saldo_final = df['Balance'].iloc[-1]

print("\n--- 💰 RELATÓRIO FINANCEIRO COMPLETO ---")
print(f"Total de Entradas:  R$ {total_recebido:,.2f}")
print(f"Total de Saídas:    R$ {total_gasto:,.2f}")
print(f"Saldo Final:        R$ {saldo_final:,.2f}")
print("-" * 40)

# 4. Top 5 Maiores Gastos
print("\n🔥 TOP 5 MAIORES GASTOS:")
gastos = df[df['Transaction Amount'] < 0].sort_values(by='Transaction Amount')
print(gastos[['Date', 'Description', 'Transaction Amount']].head())

# 5. Criar Gráfico por Categoria
print("\n📊 Gerando gráfico de categorias... (Aguarde a janela abrir)")
# Agrupamos apenas os gastos (valores negativos) por categoria
resumo_categorias = df[df['Transaction Amount'] < 0].groupby('Category')['Transaction Amount'].sum().abs()

# Criar o visual
plt.figure(figsize=(10, 6))
resumo_categorias.sort_values().plot(kind='barh', color='skyblue')
plt.title('Onde você mais gastou (Por Categoria)')
plt.xlabel('Total Gasto (R$)')
plt.ylabel('Categoria')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Mostra o gráfico na tela
plt.tight_layout()
plt.show()