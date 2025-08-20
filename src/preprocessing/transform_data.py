import os
import json
import pandas as pd

RAW_DIR = "../../data/raw"
CLEAN_DIR = "../../data/cleaned"
os.makedirs(CLEAN_DIR, exist_ok=True)

def process_json_file(filepath):
    """Extracts useful match-level info from a single JSON file."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    info = data.get("info", {})
    outcome = info.get("outcome", {})

    return {
        "match_id": os.path.basename(filepath).replace(".json", ""),
        "date": info.get("dates", [""])[0],
        "venue": info.get("venue", ""),
        "teams": ", ".join(info.get("teams", [])),
        "match_type": info.get("match_type", ""),
        "toss_winner": info.get("toss", {}).get("winner", ""),
        "toss_decision": info.get("toss", {}).get("decision", ""),
        "winner": outcome.get("winner", ""),
        "player_of_match": ", ".join(info.get("player_of_match", [])),
    }

def process_folder(match_type):
    """Processes all JSON files for a given match type into a CSV."""
    folder_path = os.path.join(RAW_DIR, match_type)
    records = []

    for file in os.listdir(folder_path):
        if file.endswith(".json"):
            file_path = os.path.join(folder_path, file)
            record = process_json_file(file_path)
            records.append(record)

    df = pd.DataFrame(records)
    out_path = os.path.join(CLEAN_DIR, f"{match_type}_matches.csv")
    df.to_csv(out_path, index=False)
    print(f"✅ Saved {len(df)} records to {out_path}")

def main():
    for match_type in os.listdir(RAW_DIR):
        if os.path.isdir(os.path.join(RAW_DIR, match_type)):
            process_folder(match_type)

if __name__ == "__main__":
    main()
    print("🎯 All cleaned CSVs saved in data/cleaned/")
