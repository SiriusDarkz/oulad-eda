# OULAD - Exploratory Data Analysis (EDA)

Este proyecto realiza un **Análisis Exploratorio de Datos (EDA)** sobre el dataset **Open University Learning Analytics Dataset (OULAD)**, con el fin de comprender mejor los patrones de comportamiento y rendimiento de los estudiantes de una universidad a distancia.

---

## Objetivo

Analizar y visualizar los datos educativos para:

- Comprender los factores que influyen en el desempeño y abandono de los estudiantes.
- Identificar patrones de comportamiento de aprendizaje según género, edad, nivel educativo y otras variables clave.
- Apoyar futuras iniciativas de predicción o intervención educativa.

---

## 🗃Dataset

**OULAD** es un dataset real publicado por The Open University, que contiene información sobre más de 30,000 estudiantes, incluyendo:

- Datos demográficos
- Resultados académicos
- Registros de interacción en la plataforma virtual (VLE)
- Información sobre módulos y cursos

> Fuente oficial del dataset: [https://analyse.kmi.open.ac.uk/open_dataset](https://analyse.kmi.open.ac.uk/open_dataset)

---

## Descarga del dataset

** Importante:**  
Por limitaciones de espacio y políticas de GitHub, **los archivos CSV del dataset no están incluidos directamente en este repositorio**.

Para ejecutar correctamente los notebooks, deberás descargar los datos manualmente:

1. Accede a la página oficial del dataset:  
    [https://analyse.kmi.open.ac.uk/open_dataset](https://analyse.kmi.open.ac.uk/open_dataset)

2. Descarga el archivo ZIP completo:  
   `oulad.zip`

3. Extrae el contenido y coloca los archivos `.csv` dentro de la carpeta `data/` del repositorio, siguiendo esta estructura:

   ```bash
   oulad-eda/
   └── data/
       ├── assessments.csv
       ├── courses.csv
       ├── studentAssessment.csv
       ├── studentInfo.csv
       ├── studentRegistration.csv
       ├── studentVle.csv
       ├── vle.csv
       └── ...

Una vez descargados y ubicados correctamente, podrás ejecutar los notebooks sin problemas.
## 🛠 Tecnologías utilizadas

- **Python 3.11+**
- **Jupyter Notebook** – Para el análisis interactivo
- **Pandas** – Manejo y análisis de datos tabulares
- **NumPy** – Operaciones numéricas
- **Matplotlib** – Visualizaciones básicas
- **Seaborn** – Visualizaciones estadísticas avanzadas
- **Plotly (opcional)** – Visualizaciones interactivas
- **Rich**
- **Postgres**
- **Poetry**
- **Conda**

---

