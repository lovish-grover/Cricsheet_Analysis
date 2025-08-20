import os
import requests
import zipfile

# -------- CONFIG --------
BASE_URL = "https://cricsheet.org/downloads/"
ZIP_FILES = {
    "test": "tests_json.zip",
    "odi": "odis_json.zip",
    "t20": "t20s_json.zip",
    "ipl": "ipl_json.zip"
}

SAVE_DIR = "../../data/raw"
os.makedirs(SAVE_DIR, exist_ok=True)

def download_and_extract(match_type, zip_name):
    """Download and extract zip file for a given match type."""
    url = BASE_URL + zip_name
    folder = os.path.join(SAVE_DIR, match_type)
    os.makedirs(folder, exist_ok=True)

    zip_path = os.path.join(SAVE_DIR, zip_name)

    # Download ZIP if not already present
    if not os.path.exists(zip_path):
        print(f"⬇️ Downloading {match_type.upper()} data from {url}")
        r = requests.get(url, stream=True)
        with open(zip_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"✅ Downloaded: {zip_path}")
    else:
        print(f"✔️ Already downloaded: {zip_path}")

    # Extract ZIP
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(folder)
    print(f"📂 Extracted {match_type.upper()} matches to {folder}")


def main():
    for match_type, zip_name in ZIP_FILES.items():
        download_and_extract(match_type, zip_name)

if __name__ == "__main__":
    main()
    print("🎯 All JSONs downloaded and extracted into data/raw/")
