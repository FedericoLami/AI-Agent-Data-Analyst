import anthropic
from dotenv import load_dotenv
from herramientas import obtener_estadisticas,comparar_grupos,contar_por_categoria,filtrar_y_analizar

load_dotenv()
client = anthropic.Anthropic()

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

def ejecutar_agente(pregunta):
    mensajes = [{"role": "user", "content": pregunta}]
    fin = False
    
    herramientas_map = {
        "obtener_estadisticas": obtener_estadisticas,
        "comparar_grupos": comparar_grupos,
        "contar_por_categoria": contar_por_categoria,
        "filtrar_y_analizar": filtrar_y_analizar
    }

    while not fin:
        answer = client.messages.create(
                    model = "claude-haiku-4-5",
                    max_tokens = 1024,
                    system = """
                             Sos un agente de analisis de datos en el dataset de RRHH de IBM.
                             Tenes acceso a las herramientas para realizar el analisis del dataset.
                             Usa las herramientas necesarias para responder preguntas sobre attrition,
                             satisfaccion laboral, salarios y otros indicadores del dataset.
                             IMPORTANTE: Nunca hagas preguntas de seguimiento al final de tus respuestas. Nunca sugieras análisis adicionales. Responde únicamente lo que se te preguntó y terminá ahí.
                             Las columnas disponibles son TODAS las del dataset IBM HR:
                             Age, Attrition, BusinessTravel, DailyRate, Department, DistanceFromHome,
                             Education, EducationField, EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, 
                             JobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate, NumCompaniesWorked, 
                             OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StockOptionLevel, TotalWorkingYears, 
                             TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager 
                            """,
                    messages = mensajes,
                    tools = tools
                )
        
        if answer.stop_reason == "end_turn":
            fin = True
            return answer.content[0].text
        elif answer.stop_reason == "tool_use":
            mensajes.append({"role" : "assistant","content" : answer.content})
            
            for bloque in answer.content:
                if bloque.type == "tool_use":
                    nombre = bloque.name    
                    argumentos = bloque.input
                    id_herramienta = bloque.id
                    resultado = herramientas_map[nombre](**argumentos)
                    mensajes.append({
                        "role": "user",
                        "content": [{
                            "type": "tool_result",
                            "tool_use_id": id_herramienta,
                            "content": resultado
                        }]
                    })
                
