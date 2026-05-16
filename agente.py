import anthropic

tools = [
    {
        "name" : "obtener_estadisticas",
        "description" : "Obtiene los datos estadisticos de la columna pasada por parametro",
        "input_schema": {
            "type": "object",
            "properties": {
                "columna": {
                    "type": "string",
                    "description": "Nombre de la columna del dataset a analizar. Age, MonthlyIncome, Department, Attrition, JobSatisfaction"
                }
            },
            "required": ["columna"]
        }
    },
    {
        "name" : "comparar_grupos",
        "description" : "Saca la media del valor de una columna agrupada",
        "input_schema": {
            "type": "object",
            "properties": {
                "columna_grupo": {
                    "type": "string",
                    "description": "Nombre de la columna del dataset a agrupar: Age, MonthlyIncome, Department, Attrition, JobSatisfaction"
                },
                "columna_valor": {
                                        "type": "string",
                    "description": "Nombre de la columna del dataset a tomar el valor: Age, MonthlyIncome, Department, Attrition, JobSatisfaction"
                }
            },
            "required": ["columna_grupo","columna_valor"]
        }
    },
    {
        "name" : "filtrar_y_analizar",
        "description" : "Filtra y analiza los datos por categoría y retorna una descripcion estadistica del parametro columna_analisis",
        "input_schema": {
            "type": "object",
            "properties": {
                "filtro_columna": {
                    "type": "string",
                    "description": "Nombre de la columna a filtrar del dataset: Age, MonthlyIncome, Department, Attrition, JobSatisfaction"
                },
                "filtro_valor": {
                    "type": "string",
                    "description": "Nombre de la columna del dataset a tomar el valor: Age, MonthlyIncome, Department, Attrition, JobSatisfaction"
                },
                "columna_analisis": {
                    "type": "string",
                    "description": "Nombre de la columna del dataset a tomar el valor: Age, MonthlyIncome, Department, Attrition, JobSatisfaction"
                }
            },
            "required": ["filtro_columna", "filtro_valor", "columna_analisis"]
        }
    },
    {
        "name" : "contar_por_categoria",
        "description" : "Cuenta el total de valores de la columna 'attrition'",
        "input_schema": {
            "type": "object",
            "properties": {
                "columna": {
                    "type": "string",
                    "description": "Nombre de la columna del dataset a analizar. Age, MonthlyIncome, Department, Attrition, JobSatisfaction"
                }
            },
            "required": ["columna"]
        }
    }
]


