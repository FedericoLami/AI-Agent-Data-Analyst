import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

def obtener_estadisticas(columna):
    if (df[columna].dtype == object):
        datos = df[columna].value_counts().to_string()
    else:
        datos = df[columna].describe().to_string()
    return datos

def comparar_grupos(columna_grupo,columna_valor):
    if pd.api.types.is_numeric_dtype(df[columna_valor]):
        datos = df.groupby(columna_grupo)[columna_valor].mean().to_string()
    else:
        datos = df.groupby(columna_grupo)[columna_valor].value_counts().to_string()
    return datos

def contar_por_categoria(columna):
    datos = df.groupby(columna)['Attrition'].value_counts(normalize = True).to_string()
    return datos

def filtrar_y_analizar(filtro_columna, filtro_valor, columna_analisis):
    datos = df[df[filtro_columna]==filtro_valor]
    
    if (df[columna_analisis].dtype == object):
        return datos[columna_analisis].value_counts().to_string()
    else:
        return datos[columna_analisis].describe().to_string()
    