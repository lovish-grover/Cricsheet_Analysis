import os
import pandas as pd
from sqlalchemy import create_engine

# -------- CONFIG --------
DB_URI = "mysql+mysqlconnector://root:mysql@localhost/cricsheet_db"  # change user/pass
CLEAN_DIR = "../../data/cleaned"

engine = create_engine(DB_URI)

def load_csv_to_mysql(filename, table_name):
    filepath = os.path.join(CLEAN_DIR, filename)
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
        print(f"Inserted {len(df)} records into {table_name}")
    else:
        print(f"File not found: {filepath}")

def main():
    load_csv_to_mysql("test_matches.csv", "test_matches")
    load_csv_to_mysql("odi_matches.csv", "odi_matches")
    load_csv_to_mysql("t20_matches.csv", "t20_matches")
    load_csv_to_mysql("ipl_matches.csv", "ipl_matches")

if __name__ == "__main__":
    main()
    print("🎯 All cleaned CSVs inserted into MySQL")
