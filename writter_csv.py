import csv

def save_csv(file_path, keyword, hits):
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["keyword", "result"])  # ヘッダー

        for item in hits:
            writer.writerow([keyword, item])