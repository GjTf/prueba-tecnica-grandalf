from pathlib import Path
import os
# ──────────────────────────────────────────────────────────────────────────────
# Rutas base ────────────────────
# ──────────────────────────────────────────────────────────────────────────────

# Carpeta raíz del proyecto
PROJECT_ROOT: Path = Path(r" ") #aqui va la ruta

# Datos crudos (CSV original)
RAW_CSV_PATH: Path = PROJECT_ROOT / "DATA" / "dataset_salud_500k.csv"

# Carpeta para datos procesados / limpiezas
CLEAN_DATA_DIR: Path = PROJECT_ROOT / "DATA"
CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)  # Crea si no existe

# Salidas estándar
CLEAN_PARQUET_PATH: Path = CLEAN_DATA_DIR / "clean_dataset.parquet"

# ──────────────────────────────────────────────────────────────────────────────
# Conexion a la base de datos ────────────────────
# ──────────────────────────────────────────────────────────────────────────────

PG_USER = os.getenv("PG_USER", "postgres")
PG_PASS = os.getenv("PG_PASS", "1234")
PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
PG_DB   = os.getenv("PG_DB",   "postgres")

PG_URI = f"postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}"
# ──────────────────────────────────────────────────────────────────────────────
# Helpers  ─────────────────────────────────────────────────────────────────────
# ──────────────────────────────────────────────────────────────────────────────

def describe_paths() -> None:
    """Imprime las rutas actuales para verificación rápida."""
    print("PROJECT_ROOT:", PROJECT_ROOT)
    print("RAW_CSV_PATH:", RAW_CSV_PATH)
    print("CLEAN_DATA_DIR:", CLEAN_DATA_DIR)
    print("CLEAN_PARQUET_PATH:", CLEAN_PARQUET_PATH)
    


def ensure_dirs() -> None:
    """Asegura que las carpetas necesarias existan."""
    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    describe_paths()
    

print(describe_paths())
