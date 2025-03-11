import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./ElementosBasicosEstadistica/housing.csv")

columnas = ["median_house_value", "total_bedrooms", "population"]

estadisticas = pd.DataFrame({
    "Columna": columnas,
    "Media": [df[col].mean() for col in columnas],
    "Mediana": [df[col].median() for col in columnas],
    "Moda": [df[col].mode()[0] if not df[col].mode().empty else "No disponible" for col in columnas],
    "Rango": [df[col].max() - df[col].min() for col in columnas],
    "Varianza": [df[col].var() for col in columnas],
    "Desviación Estándar": [df[col].std() for col in columnas]
})

print("\nEstadísticas Descriptivas:")
print(estadisticas)

for col in columnas:
    print(f"\nTabla de Frecuencias para {col}:")
    print(df[col].value_counts().reset_index().head(10))

plt.figure(figsize=(12, 6))
plt.hist(df["median_house_value"], bins=30, alpha=0.5, color="blue", label="median_house_value")
plt.hist(df["total_bedrooms"], bins=30, alpha=0.5, color="red", label="total_bedrooms")
plt.hist(df["population"], bins=30, alpha=0.5, color="green", label="population")

plt.axvline(df["median_house_value"].mean(), color='black', linestyle='dashed', linewidth=2, label='Promedio median_house_value')

plt.legend()
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Histograma comparativo de median_house_value, total_bedrooms y population")
plt.show()
