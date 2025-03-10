import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./ElementosBasicosEstadistica/housing.csv")

columnas = ["median_house_value", "total_bedrooms", "population"]

for col in columnas:
    print(f"\nEstadísticas para {col}:")
    print("Media:", df[col].mean())
    print("Mediana:", df[col].median())
    print("Moda:", df[col].mode()[0] if not df[col].mode().empty else "No disponible")
    print("Rango:", df[col].max() - df[col].min())
    print("Varianza:", df[col].var())
    print("Desviación Estándar:", df[col].std())

    tabla_frecuencia = df[col].value_counts().reset_index()
    tabla_frecuencia.columns = [col, "Frecuencia"]
    print(f"\nTabla de Frecuencias para {col}:")
    print(tabla_frecuencia.head(10))

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
