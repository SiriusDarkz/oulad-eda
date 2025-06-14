import os

class OULADPipeline:
    def __init__(self):
        self.scripts = {
            "1": "oulad.etl.create_tables",
            "2": "oulad.etl.load_raw_tables",
            "3": "oulad.etl.transform",
            "4": "oulad.etl.create_views",
            "5": "oulad.etl.drop_all_tables"
        }

    def ejecutar(self, script_path):
        print(f"Ejecutando: {script_path}")
        os.environ["PYTHONPATH"] = os.path.abspath("src")
        os.system(f"python -m {script_path}")

    def menu(self):
        while True:
            print("\n===== OULAD PIPELINE =====")
            print("1. Crear tablas RAW y Clean")
            print("2. Cargar datos RAW")
            print("3. Transformar datos (imputar, codificar, features y carga.)")
            print("4. Crear Views (Full Domain.)")
            print("5. Borrar todas las tablas (RAW y CLEAN) y Views")
            print("0. Salir")

            option = input("Seleccione una opción: ")
            if option in self.scripts:
                self.ejecutar(self.scripts[option])
            elif option == "0":
                print("👋 Saliendo del pipeline.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    pipeline = OULADPipeline()
    pipeline.menu()