"""src/etl.py
Carga el dataset limpio a PostgreSQL empleando exclusivamente la interfaz de
pandas (`read_parquet`, transformaciones DataFrame y `to_sql`).
"""
import sys, pathlib
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

import os
from datetime import datetime
from SRC.config import CLEAN_PARQUET_PATH
from SRC.config import PG_URI
import pandas as pd
from sqlalchemy import create_engine

# ---------------------------------------------------------------------------
# 1. Conexión a PostgreSQL
# ---------------------------------------------------------------------------
engine = create_engine(PG_URI, pool_pre_ping=True)

# ---------------------------------------------------------------------------
# 2. Leer dataset limpio (Parquet) y seleccionar columnas finales
# ---------------------------------------------------------------------------
print(f"[{datetime.now():%H:%M:%S}] Leyendo {CLEAN_PARQUET_PATH} …")
df = pd.read_parquet(CLEAN_PARQUET_PATH)

final_cols = [
    "patient_id", "age", "gender", "visit_date", "specialty", "diagnosis",
    "procedure", "doctor_id", "hospital_id", "city", "country",
    "visit_type", "visit_duration_minutes", "outcome",
    "readmission_within_30_days", "cost_usd",
]

missing = set(final_cols) - set(df.columns)
if missing:
    raise ValueError(f"Columnas faltantes: {missing}")

df = df[final_cols]
print(f"Filas a insertar: {len(df):,}")

# ---------------------------------------------------------------------------
# 3. Inserción con pandas.to_sql
# ---------------------------------------------------------------------------
print(f"[{datetime.now():%H:%M:%S}] Insertando en PostgreSQL …")
df.to_sql(
    name="atenciones_medicas",
    con=engine,
    schema="public",
    if_exists="append",
    index=False,
    chunksize=10_000,  # carga por lotes
    method="multi",   # inserta en batch
)

print(f"[{datetime.now():%H:%M:%S}] Carga completada – filas insertadas: {len(df):,}")
