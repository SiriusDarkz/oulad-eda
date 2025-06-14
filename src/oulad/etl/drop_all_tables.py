from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://oulad_user:oulad_pass@localhost:5432/oulad_db"
engine = create_engine(DATABASE_URL)

def drop_all_tables(engine):
    drop_statements = [
        "DROP TABLE IF EXISTS student_vles_raw CASCADE;",
        "DROP TABLE IF EXISTS vles_raw CASCADE;",
        "DROP TABLE IF EXISTS student_assessments_raw CASCADE;",
        "DROP TABLE IF EXISTS assessments_raw CASCADE;",
        "DROP TABLE IF EXISTS student_registrations_raw CASCADE;",
        "DROP TABLE IF EXISTS student_infos_raw CASCADE;",
        "DROP TABLE IF EXISTS courses_raw CASCADE;",

        "DROP TABLE IF EXISTS student_vles CASCADE;",
        "DROP TABLE IF EXISTS vles CASCADE;",
        "DROP TABLE IF EXISTS student_assessments CASCADE;",
        "DROP TABLE IF EXISTS assessments CASCADE;",
        "DROP TABLE IF EXISTS student_registrations CASCADE;",
        "DROP TABLE IF EXISTS student_infos CASCADE;",
        "DROP TABLE IF EXISTS courses CASCADE;",

        "DROP VIEW IF EXISTS fd_student_vle;",
        "DROP MATERIALIZED VIEW IF EXISTS fd_student_assessments;"
    ]

    with engine.connect() as conn:
        for stmt in drop_statements:
            print(f"Ejecutando: {stmt.strip()}")
            conn.execute(text(stmt))
        conn.commit()
    print("Todas las tablas RAW y CLEAN fueron eliminadas.")

if __name__ == "__main__":
    drop_all_tables(engine)
