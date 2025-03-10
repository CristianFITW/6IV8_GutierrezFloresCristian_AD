import pandas as pd
import matplotlib.pyplot as pit

df = pd.read_csv("./ElementosBasicosEstadistica/housing.csv")

##Mostrar las primeras 5 filas
print(df.head())

##Mostrar las ultimas 5 filas
print(df.tail())

##Mostrar fila en especificio
print(df.iloc[7])

##Mostrar rango de filas en especificio
print(df.iloc[7-10])

##Mostrar la columnaocean_proximity
print(df["ocean_proximity"])

##Obtener la media de la columna total_rooms
mediadecuarto = df["total_rooms"].mean()
print("La media del total room es: ")
print(mediadecuarto)

##Obtener la mediana
medianadecuarto = df["median_house_value"].median()
print("La mediana de la columna valor mediana de la casa: ")
print(medianadecuarto)

##La suma de popular
salariototal = df["population"].sum()
print("El salario total es de: ")
print(salariototal)

##Para poder filtrar
vamoshacerunfiltro = df[df["ocean_proximity"] == "ISLAND"]
print(vamoshacerunfiltro)

##Vamos a hacer un grafico de dispersion
pit.scatter(df["ocean_proximity"][:10], df["median_house_value"][:10])
##Nombres de los ejes
pit.xlabel("Proximidad")
pit.ylabel("Precio")

pit.tittle("Grafico de Disepersion de Proximidad al Oceano vs Precio")
pit