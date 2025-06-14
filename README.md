# OULAD - Exploratory Data Analysis (EDA)

Este proyecto realiza un **Análisis Exploratorio de Datos (EDA)** sobre el dataset **Open University Learning Analytics Dataset (OULAD)**, con el fin de comprender mejor los patrones de comportamiento y rendimiento de los estudiantes de una universidad a distancia.

---

## 📊 Objetivo

Analizar y visualizar los datos educativos para:

- Comprender los factores que influyen en el desempeño y abandono de los estudiantes.
- Identificar patrones de comportamiento de aprendizaje según género, edad, nivel educativo y otras variables clave.
- Apoyar futuras iniciativas de predicción o intervención educativa.

---

## 🗃️ Dataset

**OULAD** es un dataset real publicado por The Open University, que contiene información sobre más de 30,000 estudiantes, incluyendo:

- Datos demográficos
- Resultados académicos
- Registros de interacción en la plataforma virtual (VLE)
- Información sobre módulos y cursos

> Fuente oficial del dataset: [https://analyse.kmi.open.ac.uk/open_dataset](https://analyse.kmi.open.ac.uk/open_dataset)

---

## 🛠 Tecnologías utilizadas

- **Python 3.8+**
- **Jupyter Notebook** – Para el análisis interactivo
- **Pandas** – Manejo y análisis de datos tabulares
- **NumPy** – Operaciones numéricas
- **Matplotlib** – Visualizaciones básicas
- **Seaborn** – Visualizaciones estadísticas avanzadas
- **Plotly (opcional)** – Visualizaciones interactivas
- **Peewee (en utils)** – Exploración con ORM en versiones extendidas

---

## 📁 Estructura del proyecto

```bash
oulad-eda/
│
├── data/               # Archivos CSV originales del dataset
├── notebooks/          # Notebooks del análisis exploratorio
│   ├── assess_eda.ipynb
│   ├── vle_eda.ipynb
│   └── full_domain_eda.ipynb
├── utils/              # Funciones auxiliares y reutilizables
│   └── utils.py
├── outputs/            # Gráficos generados y tablas resumen
├── README.md           # Este archivo
└── requirements.txt    # Paquetes necesarios
