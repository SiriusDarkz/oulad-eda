from sqlalchemy import create_engine
import pandas as pd
from pathlib import Path

# URI de conexión a PostgreSQL
DB_URI = "postgresql+psycopg2://oulad_user:oulad_pass@localhost:5432/oulad_db"
engine = create_engine(DB_URI)

# Directorio donde están los CSV
CSV_DIR = Path("data")

# Map de archivos a tablas
CSV_TO_TABLE = {
    "courses.csv": "courses_raw",
    "studentInfo.csv": "student_infos_raw",
    "assessments.csv": "assessments_raw",
    "studentAssessment.csv": "student_assessments_raw",
    "studentRegistration.csv": "student_registrations_raw",
    "vle.csv": "vles_raw",
    "studentVle.csv": "student_vles_raw"
}

# Preprocesamiento si es necesario
def preprocesar_dataframe(nombre_csv, df):
    if "is_banked" in df.columns:
        df["is_banked"] = df["is_banked"].astype(bool)
    return df

# Cargar los CSV a PostgreSQL
def cargar_con_sqlalchemy():
    for nombre_csv, nombre_tabla in CSV_TO_TABLE.items():
        csv_path = CSV_DIR / nombre_csv
        print(f"Cargando: {csv_path} -> {nombre_tabla}")

        df = pd.read_csv(csv_path)
        df = preprocesar_dataframe(nombre_csv, df)

        df.to_sql(nombre_tabla, engine, if_exists="append", index=False)
        print(f"Datos insertados en {nombre_tabla} ({len(df)} filas)")

if __name__ == "__main__":
    cargar_con_sqlalchemy()