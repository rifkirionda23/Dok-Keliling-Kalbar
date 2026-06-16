import csv
import json

input_csv = "data/lokasi_foto.csv"
output_json = "data/lokasi_foto.json"

data = []

with open(input_csv, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")  # ← PENTING
    for row in reader:
        row["lat"] = float(row["lat"])
        row["lon"] = float(row["lon"])
        data.append(row)

with open(output_json, "w", encoding="utf-8") as jsonfile:
    json.dump(data, jsonfile, indent=2, ensure_ascii=False)

print("✅ CSV berhasil dikonversi ke JSON")
