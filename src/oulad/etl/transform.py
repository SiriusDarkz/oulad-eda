import pandas as pd
from sqlalchemy import create_engine
from oulad.etl.imputation import apply_null_imputations
from oulad.etl.imputation import apply_format_to_imd_band_field
from oulad.etl.encoder import apply_all_encodings
from oulad.etl.derived_features import apply_features
from rich.console import Console
from rich.panel import Panel
from rich.progress import track

DATABASE_URL = "postgresql://oulad_user:oulad_pass@localhost:5432/oulad_db"
engine = create_engine(DATABASE_URL)

console = Console()

def process_table(table_name: str, engine, extra_data: dict = {}):
    console.rule(f"[bold blue]📦 Procesando: [cyan]{table_name}[/cyan]")

    try:
        df = pd.read_sql_table(table_name + "_raw", con=engine)

        df = apply_null_imputations(df, table_name)

        if table_name == "student_infos":
            df = apply_format_to_imd_band_field(df)

        df = apply_all_encodings(df, table_name)
        df = apply_features(df, table_name, **extra_data)

        df.to_sql(table_name, con=engine, if_exists="append", index=False)

        console.print(f"[green]Tabla '[bold]{table_name}[/bold]' procesada y guardada.[/green]")
        console.print(Panel.fit(f"✔️ Filas insertadas: {len(df)}", style="green"))

    except Exception as e:
        console.print(f"[red]Error al procesar {table_name}: {e}[/red]")

def main():
    
    tables = [
        "courses",
        "student_infos",
        "student_registrations",
        "assessments",
        "student_assessments",
        "vles",
        "student_vles"
    ]

    for table in tables:
        extras = {}
        if table == "student_assessments":
            assessments_df = pd.read_sql_table("assessments", con=engine)
            extras["assessments_df"] = assessments_df
        if table == "student_vles":
            vle_df = pd.read_sql_table("vles", con=engine)
            extras["vle_df"] = vle_df

        process_table(table, engine, extras)

if __name__ == "__main__":
    main()