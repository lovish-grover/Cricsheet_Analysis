import os
import pandas as pd
from sqlalchemy import create_engine

# -------- CONFIG --------
DB_URI = "mysql+mysqlconnector://root:mysql@localhost/cricsheet_db"  # change credentials
EXPORT_DIR = "dashboards/data"
os.makedirs(EXPORT_DIR, exist_ok=True)

engine = create_engine(DB_URI)

TABLES = ["test_matches", "odi_matches", "t20_matches", "ipl_matches"]

def export_tables():
    for table in TABLES:
        query = f"SELECT * FROM {table}"
        df = pd.read_sql(query, engine)
        out_path = os.path.join(EXPORT_DIR, f"{table}.csv")
        df.to_csv(out_path, index=False)
        print(f"✅ Exported {table} → {out_path}")

if __name__ == "__main__":
    export_tables()
    print("🎯 All MySQL tables exported for Power BI")
