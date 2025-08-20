import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

CLEAN_DIR = "../../data/cleaned"

def load_data(file):
    return pd.read_csv(os.path.join(CLEAN_DIR, file))

def plot_win_counts(df, match_type):
    plt.figure(figsize=(8,5))
    sns.countplot(x="winner", data=df, order=df["winner"].value_counts().index)
    plt.xticks(rotation=45)
    plt.title(f"{match_type} - Team Wins")
    plt.tight_layout()
    plt.savefig(f"reports/{match_type}_wins.png")
    plt.close()

def main():
    os.makedirs("reports", exist_ok=True)

    test_df = load_data("test_matches.csv")
    odi_df = load_data("odi_matches.csv")
    t20_df = load_data("t20_matches.csv")
    ipl_df = load_data("ipl_matches.csv")

    plot_win_counts(test_df, "Test")
    plot_win_counts(odi_df, "ODI")
    plot_win_counts(t20_df, "T20")
    plot_win_counts(ipl_df, "IPL")

    # Example: Toss decision analysis
    plt.figure(figsize=(6,4))
    sns.countplot(x="toss_decision", data=odi_df)
    plt.title("ODI Toss Decision Distribution")
    plt.savefig("reports/odi_toss_decision.png")
    plt.close()

    print("🎯 Charts saved in reports/")

if __name__ == "__main__":
    main()
