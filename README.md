# Agente de Análisis de RRHH con IA

Agente inteligente de análisis de datos que responde preguntas en lenguaje natural sobre el dataset de RRHH de IBM. El agente decide autónomamente qué herramientas de análisis usar, las ejecuta con pandas, y sintetiza los resultados en una respuesta clara y accionable.

A diferencia de un chatbot tradicional, este sistema usa **tool use** — el modelo de lenguaje razona sobre la pregunta, selecciona las herramientas necesarias, las ejecuta en secuencia, y responde basándose en datos reales. Todo sin intervención humana en el proceso intermedio.

Pensado para equipos de RRHH, analistas de datos y managers que necesitan insights rápidos sobre retención de empleados, satisfacción laboral y tendencias organizacionales sin necesidad de escribir código.

---

## Demo

![Demo del agente](demo.gif)

---

## Tecnologías utilizadas

| Capa | Tecnología |
|------|-----------|
| Modelo de lenguaje | Claude Haiku (Anthropic API) |
| Tool use / Agente | Anthropic Tool Use API |
| Análisis de datos | Pandas |
| Backend / API REST | FastAPI + Uvicorn |
| Frontend | HTML · CSS · JavaScript vanilla |
| Dataset | IBM HR Analytics (1,470 empleados) |
| Configuración | python-dotenv |
| Entorno | Python 3.11 + venv |

---

## Arquitectura del proyecto

```
agente-analisis-datos/
├── herramientas.py      # Funciones de análisis con pandas
├── agente.py            # Lógica del agente con tool use
├── main.py              # Loop de consola (modo desarrollo)
├── main_api.py          # API REST con FastAPI
├── index.html           # Interfaz web
├── WA_Fn-UseC_-HR-Employee-Attrition.csv
├── .env                 # Variables de entorno (no se sube a GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

Cada archivo tiene una única responsabilidad:

- `herramientas.py` contiene las cuatro funciones de pandas que el agente puede usar para analizar el dataset.
- `agente.py` maneja el loop del agente: llama a Claude con las herramientas disponibles, ejecuta las que Claude solicita, y repite hasta obtener una respuesta final.
- `main_api.py` expone el agente como endpoint REST para que el frontend pueda consumirlo.

---

## ¿Qué es tool use?

Tool use es un patrón donde el modelo de lenguaje no solo genera texto sino que puede llamar a funciones externas. El flujo es:

```
1. Usuario hace una pregunta
2. Claude analiza qué herramienta necesita
3. Tu código ejecuta la herramienta con los argumentos que Claude especificó
4. Claude recibe el resultado y decide si necesita otra herramienta
5. Repite hasta tener suficiente información para responder
6. Claude sintetiza una respuesta final
```

El usuario solo ve la pregunta y la respuesta. Todo el proceso intermedio es invisible.

---

## Herramientas disponibles

| Herramienta | Descripción |
|------------|------------|
| `obtener_estadisticas(columna)` | Estadísticas descriptivas de cualquier columna |
| `comparar_grupos(columna_grupo, columna_valor)` | Compara valores entre grupos |
| `contar_por_categoria(columna)` | Distribución de attrition por categoría |
| `filtrar_y_analizar(filtro_columna, filtro_valor, columna_analisis)` | Filtra el dataset y analiza una columna específica |

---

## Ejemplos de preguntas

- ¿Qué departamento tiene mayor tasa de attrition?
- ¿Cuál es el promedio de salario mensual por nivel de trabajo?
- ¿Los empleados con overtime tienen más probabilidad de irse?
- ¿Qué relación hay entre años en la empresa y attrition?
- Analizá la satisfacción laboral del departamento de Sales
- ¿Los empleados que viajan frecuentemente tienen más attrition?

---

## Endpoints de la API

### `POST /analizar`

Recibe una pregunta en lenguaje natural y devuelve el análisis del agente.

**Request:**
```json
{
  "mensaje": "¿Qué departamento tiene mayor tasa de attrition?"
}
```

**Response:**
```
"El departamento de Sales tiene la mayor tasa de attrition con 20.6%..."
```

---

## Instalación y uso

### Requisitos previos

- Python 3.11
- API Key de Anthropic ([console.anthropic.com](https://console.anthropic.com))
- Dataset IBM HR Analytics (`WA_Fn-UseC_-HR-Employee-Attrition.csv`)

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/agente-analisis-datos.git
cd agente-analisis-datos

# 2. Crear y activar entorno virtual
py -3.11 -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
# Crear archivo .env en la raíz del proyecto:
ANTHROPIC_API_KEY=tu-api-key-aquí

# 5. Agregar el dataset CSV en la carpeta del proyecto

# 6. Iniciar el servidor
uvicorn main_api:app --reload
```

### Interfaz web

Con el servidor corriendo, abrí `index.html` directamente en el navegador.

### Modo consola

Para usar el agente sin frontend:

```bash
python main.py
```

### Documentación interactiva de la API

```
http://127.0.0.1:8000/docs
```

---

## Casos de uso empresariales

- **Retención de talento:** identificar patrones de attrition por departamento, rol o nivel para intervenir proactivamente.
- **Compensación:** analizar la relación entre salario, satisfacción y rotación para calibrar la política salarial.
- **Bienestar laboral:** detectar correlaciones entre overtime, work-life balance y attrition para mejorar condiciones de trabajo.
- **Planificación de RRHH:** anticipar qué perfiles tienen mayor riesgo de rotación y priorizar acciones de retención.

---

## Autor

**Federico Lami**
[LinkedIn](https://www.linkedin.com/in/federicolami/)