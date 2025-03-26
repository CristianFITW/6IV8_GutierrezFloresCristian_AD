import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

archivo_ventas = "proyecto1.xlsx"
archivo_sucursales = "Catalogo_sucursal.xlsx"
datos_ventas = pd.read_excel(archivo_ventas, sheet_name="in")
datos_sucursales = pd.read_excel(archivo_sucursales, sheet_name="in")

if "B_mes" in datos_ventas.columns:
    datos_ventas["B_mes"] = pd.to_datetime(datos_ventas["B_mes"], errors='coerce')

datos_ventas = datos_ventas.merge(datos_sucursales, on="id_sucursal", how="left")

ventas_totales = datos_ventas["ventas_tot"].sum()

clientes_con_adeudo = datos_ventas[datos_ventas["B_adeudo"] == "Con adeudo"]["no_clientes"].sum()
clientes_sin_adeudo = datos_ventas[datos_ventas["B_adeudo"] == "Sin adeudo"]["no_clientes"].sum()

total_clientes = clientes_con_adeudo + clientes_sin_adeudo
porcentaje_con_adeudo = (clientes_con_adeudo / total_clientes) * 100
porcentaje_sin_adeudo = (clientes_sin_adeudo / total_clientes) * 100

deuda_total = datos_ventas["adeudo_actual"].sum()

porcentaje_utilidad = ((ventas_totales - deuda_total) / ventas_totales) * 100

fig, ax = plt.subplots(figsize=(10,5))
df_ventas = datos_ventas.groupby("B_mes")["ventas_tot"].sum()
df_ventas.plot(kind="bar", ax=ax, title="Ventas Totales por Mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas Totales")
ax.set_xticklabels(df_ventas.index.strftime('%Y-%m'), rotation=45)
plt.show()

fig, ax = plt.subplots(figsize=(10,5))
df_pagos_std = datos_ventas.groupby("B_mes")["pagos_tot"].std()
df_pagos_std.plot(kind="bar", ax=ax, title="Desviación Estándar de Pagos por Mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Desviación Estándar")
ax.set_xticklabels(df_pagos_std.index.strftime('%Y-%m'), rotation=45)
plt.show()

df_ventas_sucursal = datos_ventas.groupby("suc")["ventas_tot"].sum()
df_ventas_sucursal.plot(kind="pie", autopct='%1.1f%%', figsize=(8,8), title="Distribución de Ventas por Sucursal")
plt.ylabel("")
plt.show()

df_utilidad = datos_ventas.groupby("suc").agg({"adeudo_actual": "sum", "ventas_tot": "sum"})
df_utilidad["margen_utilidad"] = ((df_utilidad["ventas_tot"] - df_utilidad["adeudo_actual"]) / df_utilidad["ventas_tot"]) * 100

fig, ax1 = plt.subplots(figsize=(10,5))
ax2 = ax1.twinx()
ax1.bar(df_utilidad.index, df_utilidad["adeudo_actual"], color='r', alpha=0.6, label="Deuda Total")
ax2.plot(df_utilidad.index, df_utilidad["margen_utilidad"], color='b', marker='o', label="Margen de Utilidad (%)")
ax1.set_xlabel("Sucursal")
ax1.set_ylabel("Deuda Total", color='r')
ax2.set_ylabel("Margen de Utilidad (%)", color='b')
plt.title("Deuda Total por Sucursal vs Margen de Utilidad")
plt.legend()
plt.show()