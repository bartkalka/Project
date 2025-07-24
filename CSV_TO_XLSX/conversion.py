import pandas as pd

# Wczytaj plik CSV w trybie przetwarzania strumieniowego
csv_file = "retail_institute_final_2024.csv"
chunk_size = 1_000_000  # Bezpieczny bufor (trochę mniej niż 1 048 576)

file_counter = 1  # Numerowanie plików

for chunk in pd.read_csv(csv_file, chunksize=chunk_size, low_memory=False):
    # Jeśli chunk jest większy niż 1 048 576 wierszy, podziel go na mniejsze części
    for start_row in range(0, len(chunk), 1_048_576):
        sub_chunk = chunk.iloc[start_row:start_row + 1_048_576]  # Podział na max 1 048 576 wierszy
        
        xlsx_file = f"output_part_{file_counter}.xlsx"  # Tworzenie nowych plików
        with pd.ExcelWriter(xlsx_file, engine='openpyxl') as writer:
            sub_chunk.to_excel(writer, sheet_name="Data", index=False)  # Każdy plik ma 1 arkusz
        
        print(f"Zapisano plik: {xlsx_file}")
        file_counter += 1  # Zwiększenie numeracji plików

print("Konwersja zakończona.")
